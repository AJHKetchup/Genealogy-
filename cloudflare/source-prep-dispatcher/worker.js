const RAW_SAMPLE_LIMIT = 25;
const R2_CONTRACT_AUDIT_LIMIT = 1000;
const R2_VIOLATION_SAMPLE_LIMIT = 20;
const GITHUB_OWNED_EXTENSIONS = [
  ".json",
  ".md",
  ".markdown",
  ".toml",
  ".yaml",
  ".yml",
  ".py",
  ".js",
  ".ts",
  ".tsx",
  ".jsx",
];

function present(value) {
  return typeof value === "string" && value.length > 0;
}

async function readSecretLike(value) {
  if (present(value)) {
    return value;
  }
  if (value && typeof value.get === "function") {
    const secret = await value.get();
    return present(secret) ? secret : "";
  }
  return "";
}

async function redactStatus(value) {
  return { present: present(await readSecretLike(value)) };
}

async function listRawSample(env) {
  if (!env.GENEALOGY_R2 || typeof env.GENEALOGY_R2.list !== "function") {
    return { ok: false, error: "GENEALOGY_R2 binding missing" };
  }

  const listing = await env.GENEALOGY_R2.list({ limit: RAW_SAMPLE_LIMIT });
  return {
    ok: true,
    truncated: Boolean(listing.truncated),
    cursor_present: Boolean(listing.cursor),
    sample_count: listing.objects.length,
    sample_objects: listing.objects.map((object) => ({
      key: object.key,
      size: object.size,
      uploaded: object.uploaded ? object.uploaded.toISOString() : null,
    })),
  };
}

function isGithubOwnedR2Key(key) {
  const normalized = key.toLowerCase();
  return (
    normalized === "manifest.json" ||
    normalized.endsWith("/manifest.json") ||
    normalized.startsWith("manifests/") ||
    normalized.includes("/manifests/") ||
    GITHUB_OWNED_EXTENSIONS.some((extension) => normalized.endsWith(extension))
  );
}

async function auditR2Contract(env) {
  if (!env.GENEALOGY_R2 || typeof env.GENEALOGY_R2.list !== "function") {
    return { ok: false, error: "GENEALOGY_R2 binding missing" };
  }

  let cursor = undefined;
  let scanned = 0;
  let violation_count = 0;
  const violation_samples = [];

  do {
    const remaining = R2_CONTRACT_AUDIT_LIMIT - scanned;
    const listing = await env.GENEALOGY_R2.list({ limit: Math.min(1000, remaining), cursor });
    for (const object of listing.objects) {
      scanned += 1;
      if (isGithubOwnedR2Key(object.key)) {
        violation_count += 1;
        if (violation_samples.length < R2_VIOLATION_SAMPLE_LIMIT) {
          violation_samples.push(object.key);
        }
      }
    }
    cursor = listing.truncated && scanned < R2_CONTRACT_AUDIT_LIMIT ? listing.cursor : undefined;
  } while (cursor && scanned < R2_CONTRACT_AUDIT_LIMIT);

  return {
    ok: violation_count === 0,
    scanned,
    capped: scanned >= R2_CONTRACT_AUDIT_LIMIT,
    violation_count,
    violation_samples,
  };
}

async function heartbeat(env, trigger) {
  const secrets = {
    GEMINI_API_KEY: await redactStatus(env.GEMINI_API_KEY),
    R2_ACCOUNT_ID: await redactStatus(env.R2_ACCOUNT_ID),
    R2_BUCKET: await redactStatus(env.R2_BUCKET),
    R2_ENDPOINT_URL: await redactStatus(env.R2_ENDPOINT_URL),
    GITHUB_TOKEN: await redactStatus(env.GITHUB_TOKEN),
    GITHUB_OWNER: await redactStatus(env.GITHUB_OWNER),
    GITHUB_REPO: await redactStatus(env.GITHUB_REPO),
  };
  const r2 = await listRawSample(env);
  const r2_contract = await auditR2Contract(env);
  const blockers = [];

  if (!secrets.GEMINI_API_KEY.present) {
    blockers.push("GEMINI_API_KEY is missing from Cloudflare secret bindings.");
  }
  if (!r2.ok) {
    blockers.push(r2.error);
  }
  if (r2_contract.ok === false && r2_contract.error) {
    blockers.push(r2_contract.error);
  } else if (r2_contract.violation_count > 0) {
    blockers.push("R2 contains GitHub-owned JSON/Markdown/code/manifest objects that should be moved out of raw/binary storage.");
  }
  if (!secrets.GITHUB_TOKEN.present || !secrets.GITHUB_OWNER.present || !secrets.GITHUB_REPO.present) {
    blockers.push("GitHub write/dispatch bindings are missing; dispatcher cannot update GitHub queue state yet.");
  }

  return {
    ok: blockers.length === 0,
    mode: "cloudflare-source-prep-dispatcher-preflight",
    trigger,
    checked_at: new Date().toISOString(),
    storage_contract: {
      r2: "raw originals and binary derivatives only",
      github: "converted Markdown plus minimal JSON manifests, queues, and task state",
    },
    secrets,
    r2,
    r2_contract,
    blockers,
    next_when_unblocked: [
      "Find raw originals in R2 that do not have converted Markdown.",
      "Convert missing one-page tasks with Gemini.",
      "Write converted Markdown and minimal JSON state to GitHub.",
      "Write page images/crops back to R2 when they are binary derivatives.",
    ],
  };
}

function jsonResponse(payload, status = 200) {
  return new Response(JSON.stringify(payload, null, 2), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
    },
  });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/" || url.pathname === "/health" || url.pathname === "/run") {
      const payload = await heartbeat(env, `http:${request.method}:${url.pathname}`);
      return jsonResponse(payload, payload.ok ? 200 : 424);
    }
    return jsonResponse({ ok: false, error: "not_found", paths: ["/health", "/run"] }, 404);
  },

  async scheduled(event, env, ctx) {
    ctx.waitUntil(
      heartbeat(env, `cron:${event.cron}`).then((payload) => {
        console.log(JSON.stringify({
          ok: payload.ok,
          checked_at: payload.checked_at,
          sample_count: payload.r2 && payload.r2.sample_count,
          blockers: payload.blockers,
        }));
      }),
    );
  },
};

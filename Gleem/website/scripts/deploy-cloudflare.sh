#!/usr/bin/env bash
# Deploy Stillwall marketing site to Cloudflare Pages (project: yilinglabs)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPO_ROOT="$(cd "$ROOT/.." && pwd)"
cd "$ROOT"

# Load local secrets if present (never commit .env)
if [[ -f "$REPO_ROOT/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "$REPO_ROOT/.env"
  set +a
fi

# Prefer account token for wrangler when API token is missing/insufficient
if [[ -n "${CLOUDFLARE_ACCOUNT_TOKEN:-}" ]]; then
  export CLOUDFLARE_API_TOKEN="${CLOUDFLARE_ACCOUNT_TOKEN}"
fi

if ! command -v wrangler >/dev/null 2>&1; then
  echo "wrangler not found. Install: npm i -g wrangler  (or brew install cloudflare-wrangler)"
  exit 1
fi

if [[ -z "${CLOUDFLARE_API_TOKEN:-}" ]]; then
  echo "Warning: CLOUDFLARE_API_TOKEN not set. Falling back to wrangler OAuth / cached credentials."
fi

MSG="${1:-Deploy Stillwall marketing site}"
echo "Deploying $ROOT → Cloudflare Pages project 'yilinglabs'…"
wrangler pages deploy . \
  --project-name=yilinglabs \
  --branch=main \
  --commit-dirty=true \
  --commit-message="$MSG"

echo ""
echo "Production: https://yilinglabs.pages.dev"
echo "Custom:     https://yilinglabs.com  (after DNS CNAME is active)"
echo "Privacy:    https://yilinglabs.com/privacy"
echo "Support:    https://yilinglabs.com/support"

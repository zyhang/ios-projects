#!/usr/bin/env bash
# Deploy Stillwall marketing site to Cloudflare Pages (project: yilinglabs)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! command -v wrangler >/dev/null 2>&1; then
  echo "wrangler not found. Install: npm i -g wrangler  (or brew install cloudflare-wrangler)"
  exit 1
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

# Stillwall static site (Privacy / Support)

Deploy this folder to your host so App Store URLs resolve:

| ASC field | Suggested public URL | File |
|-----------|----------------------|------|
| Privacy Policy | `https://yilinglabs.com/privacy` | `privacy.html` (or rewrite); prefer live `website/privacy/` |
| Support | `https://yilinglabs.com/support` | `support.html`; prefer live `website/support/` |
| Marketing (optional) | `https://yilinglabs.com/` | `index.html` / `website/` |

## Local preview

```bash
cd docs/release/app-store-assets/site
python3 -m http.server 8765
# open http://127.0.0.1:8765/
```

## Netlify / GitHub Pages

- Publish this directory as the site root, **or**
- Add redirects: `/privacy` → `/privacy.html`, `/support` → `/support.html`

### Example `_redirects` (Netlify)

```
/privacy  /privacy.html  200
/support  /support.html  200
```

## Before go-live

1. Prefer deploying `website/` (canonical). This `site/` folder is a fallback ASC mirror.
2. Support copy must match `../copy/support-en-US.md` (no Home “On” badge; `Set Up in Safari`; 6 CB + Web Extension).
3. Confirm HTTPS on yilinglabs.com.
4. Paste final URLs into App Store Connect.

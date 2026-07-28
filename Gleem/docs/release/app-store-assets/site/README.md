# Stillwall static site (Privacy / Support)

Deploy this folder to your host so App Store URLs resolve:

| ASC field | Suggested public URL | File |
|-----------|----------------------|------|
| Privacy Policy | `https://<domain>/privacy` | `privacy.html` (or rewrite) |
| Support | `https://<domain>/support` | `support.html` |
| Marketing (optional) | `https://<domain>/` | `index.html` |

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

1. Replace `<LEGAL_ENTITY_NAME>` and `<domain>` / email addresses in the HTML (or regenerate from `../copy/*.md`).
2. Confirm HTTPS.
3. Paste final URLs into App Store Connect.

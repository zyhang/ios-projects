# Agent instructions (ios-projects)

This repository is for iOS product work under `Gleem/` (Stillwall) and related docs.

## Git workflow (mandatory)

**Always work on `main` and commit + push to `main` after meaningful changes.**

1. Stay on **`main`**. Do **not** create feature branches unless the user explicitly asks.
2. After finishing a task that changes files (docs, design exports, code, config):
   - `git add` the relevant files
   - create a commit with a clear message (complete sentences)
   - **`git push origin main`**
3. Do **not** wait for the user to say “commit” or “push” for routine completed work on this repo—**default is commit + push to `main`**.
4. Only skip commit/push when:
   - the change is a pure local experiment the user asked not to keep, or
   - there is nothing to commit, or
   - the user explicitly says not to push
5. Prefer small, focused commits over one giant dump when multiple unrelated tasks finish in one session; still push each (or batch once at end of the turn if pushes would thrash).
6. Never force-push `main` unless the user explicitly orders it.
7. Never update git config.

## Product context (Stillwall)

- Internal code name: **Gleem**
- Brand: **Stillwall**
- App Store **Name:** `Stillwall for Safari`
- App Store **Subtitle:** `Free Ad & Tracker Blocking`
- Home screen display name: `Stillwall`
- Authoritative product scope: `Gleem/docs/product/product-charter.md`
- Decisions: `Gleem/docs/decisions/decision-log.md`
- App Store package: `Gleem/docs/release/app-store-submission.md`

## Docs language

- Collaboration docs: Chinese (except identifiers, API names, and user-facing English UI/store copy).
- Do not invent “已完成 / 已验证” for work that was not actually delivered or tested.

## Post-dev issues (screens / behavior)

After the app is built, page and feature fix requests (especially from screenshots) go under **`Gleem/issues/`**:

- Rules: `Gleem/issues/AGENTS.md`
- One issue per folder: `NNN-short-slug/` (incrementing), with README + screenshots for developers
- Create/update issues there; do not leave fix instructions only in chat

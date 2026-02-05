# Wiki Publishing

This folder contains mapping and templates for publishing Markdown canon to MediaWiki.

## Environment Variables
- `MW_API_URL`
- `MW_BOT_USERNAME`
- `MW_BOT_PASSWORD`
- `MW_USER_AGENT`

## Commands
- Validate canon: `python tools/validate_canon.py`
- Publish: `python tools/publish_wiki.py`

## Notes
- Each edit summary must include the git short SHA and the file list.
- Secrets must never be committed.

# Website Uptime Monitor

A simple website uptime monitor powered by GitHub Actions.

## Status

| Website | Status | Code |
|---|---|---|
| https://amazon.com | ❌ Down | 503 |
| https://google.com | ✅ Online | 200 |

_Last checked: 2026-08-30 12:25 UTC_

## How It Works

This project checks the websites listed in `sites.txt` every 15 minutes using GitHub Actions.
It updates this README with the latest status and commits the changes automatically using `github-actions[bot]`.

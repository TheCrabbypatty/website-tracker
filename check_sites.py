from datetime import datetime, timezone
import requests

sites_file = "sites.txt"
readme_file = "README.md"

with open(sites_file, "r", encoding="utf-8") as file:
    sites = [line.strip() for line in file if line.strip()]

results = []

for site in sites:
    try:
        response = requests.get(site, timeout=10)
        if response.status_code < 400:
            results.append((site, "Online", response.status_code))
        else:
            results.append((site, "Down", response.status_code))
    except Exception:
        results.append((site, "Down", "Error"))

now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

lines = [
    "# Website Uptime Monitor",
    "",
    "A simple website uptime monitor powered by GitHub Actions.",
    "",
    "## Status",
    "",
    "| Website | Status | Code |",
    "|---|---|---|",
]

for site, status, code in results:
    emoji = "✅" if status == "Online" else "❌"
    lines.append(f"| {site} | {emoji} {status} | {code} |")

lines += [
    "",
    f"_Last checked: {now}_",
    "",
    "## How It Works",
    "",
    "This project checks the websites listed in `sites.txt` every 5 minutes using GitHub Actions.",
    "It updates this README with the latest status and commits the changes automatically using `github-actions[bot]`.",
]

with open(readme_file, "w", encoding="utf-8") as file:
    file.write("\n".join(lines) + "\n")

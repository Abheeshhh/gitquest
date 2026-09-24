"""
Refresh Leaderboard
--------------------
Reads participants.txt, fetches each participant's QUEST_LOG.md directly
from their public GitHub fork (raw.githubusercontent.com — no auth needed
for public repos), computes XP from checked boxes, and rewrites
LEADERBOARD.md grouped by team, sorted by XP.

No dependencies beyond the Python standard library.
"""

import csv
import re
import urllib.request
import urllib.error

QUEST_POINTS = {
    "Q1": 5,
    "Q2": 10,
    "Q3": 15,
    "Q4": 15,
    "Q5": 30,
    "Q6": 15,
    "Q7": 20,
    "Q8": 15,
    "Q9": 25,
    "Q10": 10,
    "Q11": 30,
    "Q12": 40,
}

CHECK_PATTERN = re.compile(r"-\s*\[(x|X)\]\s*(Q\d{1,2})\b")

FORK_REPO_NAME = "gitquest"
FORK_BRANCH = "main"


def fetch_quest_log(username):
    url = f"https://raw.githubusercontent.com/{username}/{FORK_REPO_NAME}/{FORK_BRANCH}/QUEST_LOG.md"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "gitquest-leaderboard-bot"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8"), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}"
    except Exception as e:
        return None, str(e)


def compute_xp(text):
    completed = []
    for match in CHECK_PATTERN.finditer(text):
        qid = match.group(2).upper()
        if qid in QUEST_POINTS and qid not in completed:
            completed.append(qid)
    completed.sort(key=lambda q: int(q[1:]))
    xp = sum(QUEST_POINTS[q] for q in completed)
    return xp, completed


def load_participants(path="participants.txt"):
    rows = []
    with open(path, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            first = row[0].strip()
            if not first or first.startswith("#"):
                continue
            if len(row) < 3:
                continue
            username, team, name = (x.strip() for x in row[:3])
            rows.append((username, team, name))
    return rows


def render_leaderboard(entries):
    lines = [
        "# Leaderboard (Auto-Updated)",
        "",
        "_This file is generated automatically by GitHub Actions from each participant's "
        "`QUEST_LOG.md` in their own fork. Do not edit it by hand — it will be overwritten "
        "on the next refresh._",
        "",
    ]

    teams = {}
    for entry in entries:
        teams.setdefault(entry["team"], []).append(entry)

    overall_total = sum(e["xp"] for e in entries)
    lines.append(f"**Total participants:** {len(entries)}  ")
    lines.append(f"**Combined XP across everyone:** {overall_total}")
    lines.append("")

    for team in sorted(teams):
        team_entries = sorted(teams[team], key=lambda e: -e["xp"])
        team_total = sum(e["xp"] for e in team_entries)
        lines.append(f"## {team}  (team total: {team_total} XP)")
        lines.append("")
        lines.append("| Name | GitHub | XP | Levels Completed | Status |")
        lines.append("|------|--------|----|-------------------|--------|")
        for e in team_entries:
            levels = ", ".join(e["completed"]) if e["completed"] else "-"
            status = "✅" if e["error"] is None else f"⚠️ {e['error']}"
            lines.append(
                f"| {e['name']} | [@{e['username']}](https://github.com/{e['username']}) | "
                f"{e['xp']} | {levels} | {status} |"
            )
        lines.append("")

    return "\n".join(lines) + "\n"


def main():
    participants = load_participants()
    entries = []

    for username, team, name in participants:
        text, error = fetch_quest_log(username)
        if text is None:
            entries.append(
                {"username": username, "team": team, "name": name, "xp": 0, "completed": [], "error": error}
            )
            continue
        xp, completed = compute_xp(text)
        entries.append(
            {"username": username, "team": team, "name": name, "xp": xp, "completed": completed, "error": None}
        )

    output = render_leaderboard(entries)
    with open("LEADERBOARD.md", "w") as f:
        f.write(output)

    print(f"Refreshed leaderboard for {len(entries)} participant(s).")


if __name__ == "__main__":
    main()

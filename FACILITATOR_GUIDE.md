# Facilitator Guide

## Before the day
- Push this repo to GitHub as the main/upstream repo — this is the one that has `participants.txt` and the auto-refreshed `LEADERBOARD.md`.
- **Enable Actions write access:** on the main repo, go to Settings → Actions → General → Workflow permissions → select "Read and write permissions" → Save. Without this, the bot can't commit the updated leaderboard.
- Fork model: each participant forks the upstream repo to their own account using the **Fork** button (not "Use this template", so it keeps the repo name `gitquest`), and works there. Nobody needs collaborator access to the main repo.
- **Their fork must be public** — the leaderboard reads `QUEST_LOG.md` from each fork's raw GitHub URL, which only works for public repos.
- As participants join, add a line to `participants.txt` on the main repo: `github_username,team,display_name`. You can do this by editing the file directly on GitHub, or batch-add everyone at once before the day if you already have the sign-up list.
- For Level 5 (conflict) and Level 9 (cherry-pick), pairs need each other's fork URLs to add as a git remote — have teams share these with each other at the start.
- Decide what you'll break on `main` for Level 12 (Final Boss) — write it down so you remember what "fixed" looks like.
- Test the whole flow yourself once: fork the repo under a test account, check a box in `QUEST_LOG.md`, push, add yourself to `participants.txt`, manually trigger the "Refresh Leaderboard" workflow from the Actions tab, confirm your XP shows up.

## Coordinator role during the day
- The leaderboard refreshes on its own every ~5 minutes. For a truly instant update at any moment (e.g. right before revealing standings), go to: main repo → **Actions** tab → **Refresh Leaderboard** (left sidebar) → **Run workflow** button (top right) → **Run workflow** again to confirm. It finishes in under a minute.
- For a genuinely "live" feel during the session, keep the repo's `LEADERBOARD.md` open on a projector/shared screen, and manually trigger "Run workflow" every 1–2 minutes during exciting stretches (e.g. right after the merge-conflict level) instead of relying on the schedule.
- Keep `participants.txt` updated as people join late or usernames change — the workflow re-reads it on every run.
- If a participant's row shows an error (⚠️) instead of XP, it usually means their fork isn't named `gitquest`, isn't public, or they haven't pushed `QUEST_LOG.md` yet — have them check.

### Why not truly real-time?
True instant updates the moment someone pushes would require giving every participant's fork a token with write access to the main repo (so their push can immediately trigger the main repo's workflow). That undoes the safety benefit of the fork model — anyone with that token could also push changes to the main repo, not just trigger the leaderboard. For a workshop with many participants, the 5-minute schedule plus on-demand manual trigger is the safer trade-off, and in practice feels close enough to live.

## Schedule (7 hrs)

| Time | Activity |
|------|----------|
| 9:00–9:20 | Kickoff, teams, clone repo |
| 9:20–10:15 | Levels 1–3 |
| 10:15–10:30 | Break |
| 10:30–11:30 | Levels 4–5 (conflict — help teams pair up) |
| 11:30–12:30 | Levels 6–7 |
| 12:30–1:15 | Lunch |
| 1:15–2:15 | Levels 8–9 |
| 2:15–2:30 | Break |
| 2:30–3:15 | Levels 10 |
| 3:15–4:00 | Level 11 (push/PR) |
| 4:00–4:30 | Level 12 (Final Boss — plant the bug right before this) |
| 4:30–5:00 | Freeze leaderboard, tally, prize, wrap-up |

## Tips
- Walk the room during hands-on time. Level 5 (conflict) and Level 9 (cherry-pick) trip people up most.
- Keep a prize ready for top scorer and/or top team.
- GitHub's scheduled Actions can occasionally run a few minutes late under load — if the leaderboard looks stale near the end of the day, just trigger it manually.

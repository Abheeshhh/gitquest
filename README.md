# Git Quest 🗡️

A one-day, game-based Git workshop. Teams complete levels using real git commands, track progress on a shared leaderboard, and level up.

## How to Play

1. Get into your team (3–4 people per team).
2. **Fork this repo** using the **Fork** button on GitHub — not "Use this template" — so your copy keeps the name `gitquest`. Make sure your fork is **public**.
3. Give the coordinator your GitHub username and team name so they can add you to `participants.txt` on the main repo.
4. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/gitquest.git
   cd gitquest
   ```
5. Open `QUESTS.md` and do the levels **in order**.
6. As you finish each level, open `QUEST_LOG.md` in your fork, change `[ ]` to `[x]` for that level, then:
   ```bash
   git add QUEST_LOG.md
   git commit -m "Complete Q3"
   git push
   ```
7. That's it — **no PR, no manual score submission.** The main repo automatically re-reads everyone's `QUEST_LOG.md` every few minutes and rebuilds `LEADERBOARD.md`. Check the main repo's `LEADERBOARD.md` (or ask the coordinator to trigger an instant refresh from the Actions tab) to see live standings.

All your actual git work — branches, commits, merges, stashes — happens inside your own fork. Nothing you do there can affect anyone else's fork or the main repo, except the leaderboard reading your `QUEST_LOG.md`.

## Files in this repo

- `QUESTS.md` — all levels, in order, with instructions
- `QUEST_LOG.md` — your personal checklist, in your own fork (this is what the leaderboard reads)
- `LEADERBOARD.md` — auto-generated official scoreboard on the main repo — don't edit by hand
- `participants.txt` — coordinator's registry of who's playing (main repo only)
- `teams/` — one folder per team, for shared exercises like the merge conflict level
- `FACILITATOR_GUIDE.md` — schedule and setup notes (facilitator only)

## Rules

- Do every level yourself. Don't copy a teammate's commands — type them yourself so it sticks.
- Ask for help if stuck more than 5 minutes.
- Have fun, break things on purpose sometimes — that's how you learn to fix them.

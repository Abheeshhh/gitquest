# Quests

Do these in order. Each one builds on the last. Use your own file inside `teams/<your-team>/yourname.txt`, inside YOUR OWN FORK of this repo.

After finishing a level, check it off in your own `QUEST_LOG.md` and push. The leaderboard on the main repo picks it up automatically — you don't need to tell anyone.

---

### Level 1 — Wake Up (5 pts)
Check your git identity is set correctly.
```
git config user.name
git config user.email
```
If empty, set them:
```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
**Done when:** both commands print your real name and email.

---

### Level 2 — First Save (10 pts)
Write a sentence about yourself in your file (`teams/<team>/yourname.txt`), then save it to git.
```
git add teams/<team>/yourname.txt
git commit -m "Add my intro"
git push
```
**Done when:** your commit shows up in `git log`.

---

### Level 3 — Branch Out (15 pts)
Make your own branch and save a change there.
```
git checkout -b <yourname>-feature
echo "trying a branch" >> teams/<team>/yourname.txt
git add .
git commit -m "Work on my branch"
```
**Done when:** `git branch` shows your new branch.

---

### Level 4 — Bring It Together (15 pts)
Merge your branch back into main.
```
git checkout main
git merge <yourname>-feature
git push
```
**Done when:** your branch's changes appear on main.

---

### Level 5 — The Clash (30 pts) — do with a teammate
Since you're each in your own fork, first add your teammate's fork as a second remote so you can see their branch:
```
git remote add teammate <teammate-fork-url>
git fetch teammate
```
Now you and your teammate both edit the SAME line in `teams/<team>/battle.txt`, on two different branches, then try to merge. Git will refuse and show a conflict.
```
git merge teammate/<their-branch-name>
```
Open the file, you'll see marks like `<<<<<<<`, `=======`, `>>>>>>>`. Pick what stays, delete the marks, then:
```
git add teams/<team>/battle.txt
git commit -m "Resolve conflict with <teammate>"
```
**Done when:** the file has no conflict marks left and commit succeeds.

---

### Level 6 — Save For Later (15 pts)
Start editing your file but don't finish. Stash it, switch branch, come back, restore it.
```
git stash
git checkout main
git checkout -
git stash pop
```
**Done when:** your unfinished edit is back and nothing was lost.

---

### Level 7 — Undo Button (20 pts)
Make a bad change on purpose, then undo it two different ways.

Way 1 — revert (keeps history, adds a new "undo" commit):
```
git revert <bad-commit-hash>
```
Way 2 — reset (rewrites history, use only on your own branch):
```
git reset --soft HEAD~1
```
**Done when:** you understand and can explain the difference between the two.

---

### Level 8 — Detective Work (15 pts)
Investigate your file's history.
```
git log --oneline
git blame teams/<team>/yourname.txt
git show <any-commit-hash>
```
**Done when:** you can say who changed what and when, from the output alone.

---

### Level 9 — Steal a Commit (25 pts)
Pick one specific commit from a teammate's branch and apply it to yours, without merging everything. (Reuse the `teammate` remote from Level 5, or add it now if you skipped that.)
```
git fetch teammate
git log teammate/<their-branch> --oneline
git cherry-pick <that-commit-hash>
```
**Done when:** that one change appears on your branch, nothing else from theirs does.

---

### Level 10 — Mark the Milestone (10 pts)
Tag your current commit.
```
git tag -a <yourname>-v1 -m "My first milestone"
git tag
```
**Done when:** `git tag` lists your tag.

---

### Level 11 — Send It Out (30 pts)
Push your branch to your own fork, then open a Pull Request from your branch into your fork's own main branch (or into the original upstream repo if the coordinator allows it). Get a teammate to review and approve it before merging.
```
git push -u origin <yourname>-feature
```
Then open the PR on GitHub, tag a teammate to review.
**Done when:** PR is approved and merged, and you've run `git pull` to sync.

---

### Level 12 — Final Boss (40 pts)
Facilitator will break something on the main branch. Find it and fix it.
```
git log --oneline
git diff <good-commit> <bad-commit>
```
Fix it, commit, open a PR, get it merged.
**Done when:** main branch works again and your fix is merged.

---

## Total possible: 230 pts per person

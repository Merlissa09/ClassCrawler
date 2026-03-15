# GitHub Issues Creation - Quick Visual Guide

## 📋 What You're Creating

```
Wave 1: Foundation (5 issues, 9 pts)
├── Character base class [2pts]
├── Item classes [2pts]
├── Room & Dungeon [2pts]
├── IGameRepository [1pt]
└── CI Pipeline [2pts]

Wave 2: Game Logic (8 issues, 18 pts)
├── Player class [2pts]
├── Enemy classes [2pts]
├── Combat Strategy [3pts]
├── CharacterFactory [2pts]
├── Event System [3pts]
├── Combat Engine [3pts]
├── Loot System [2pts]
└── Leveling System [2pts]

Wave 3: Integration (5 issues, 12 pts)
├── SQLite Repository [3pts]
├── Leaderboard [2pts]
├── Console UI [3pts]
├── Combat Tests [2pts]
└── Item Tests [2pts]

Total: 18 issues, 39 points
```

## 🚀 Three Ways to Create Issues

### Method 1: GitHub Actions ⭐ RECOMMENDED

```
┌─────────────────────────────────────────┐
│  1. Go to Actions tab in GitHub        │
│  2. Select "Create Project Issues"     │
│  3. Click "Run workflow"               │
│  4. Choose wave (or "all")             │
│  5. Click "Run workflow" again         │
│  6. Wait ~30 seconds                   │
│  7. Check Issues tab                   │
└─────────────────────────────────────────┘
```

**Pros**: No local setup, fully automated
**Cons**: Requires workflow permissions (should work by default)

---

### Method 2: Command Line Scripts

#### Option A: Bash Script
```bash
cd ClassCrawler
./create_issues.sh
```

#### Option B: Python Script
```bash
cd ClassCrawler
python3 create_issues.py
```

**Prerequisites**: GitHub CLI installed and authenticated
```bash
gh auth login
```

**Pros**: Fast, automated, can retry easily
**Cons**: Requires local setup and GitHub CLI

---

### Method 3: Manual Creation

```
For each issue:
1. Go to https://github.com/Merlissa09/ClassCrawler/issues
2. Click "New issue"
3. Copy title from MANUAL_ISSUE_CREATION.md
4. Copy description from MANUAL_ISSUE_CREATION.md
5. Add labels: wave-X, difficulty-Y
6. Click "Submit new issue"
7. Repeat for remaining issues
```

**Pros**: Always works, no dependencies
**Cons**: Time-consuming (15-20 minutes for all 18)

---

## 📁 Files in This PR

```
ClassCrawler/
├── .github/workflows/
│   └── create-issues.yml          ← GitHub Actions workflow
├── create_issues.sh               ← Bash script
├── create_issues.py               ← Python script
├── create_single_issue.sh         ← API helper
├── SOLUTION_SUMMARY.md            ← This guide
├── ISSUES_README.md               ← Comprehensive docs
├── MANUAL_ISSUE_CREATION.md       ← Step-by-step manual
├── VISUAL_GUIDE.md                ← Quick reference (this file)
├── issues_wave1.json              ← JSON template example
└── README.md                      ← Updated with instructions
```

## 🏷️ Labels to Create First (if needed)

| Label | Color | Description |
|-------|-------|-------------|
| wave-1 | 🟢 #0E8A16 | Foundation |
| wave-2 | 🟡 #FBCA04 | Game Logic |
| wave-3 | 🔴 #D93F0B | Integration |
| difficulty-1 | 🔵 #C5DEF5 | Easy |
| difficulty-2 | 🟣 #5319E7 | Medium |
| difficulty-3 | ⚫ #B60205 | Hard |

Create at: https://github.com/Merlissa09/ClassCrawler/labels

---

## ⚡ Quick Start

**Just want to get started?**

1. **Merge this PR**
2. **Go to Actions tab**
3. **Run "Create Project Issues" workflow**
4. **Start coding Wave 1!**

---

## 🆘 Troubleshooting

### "Workflow not found"
→ Make sure the PR is merged first
→ Check .github/workflows/ directory exists

### "Permission denied" on scripts
→ Run: `chmod +x create_issues.sh`

### "gh auth failed"
→ Run: `gh auth login` and follow prompts

### "API rate limit"
→ Wait a few minutes, authenticated requests have higher limits

### All else fails?
→ Use Method 3 (manual creation) with MANUAL_ISSUE_CREATION.md

---

## 📊 Progress Tracking

After creating issues, track them with:
- ✅ Project boards
- ✅ Milestones (one per wave)
- ✅ Acceptance criteria checklists in each issue

---

## 💡 Tips

- Create issues **in wave order** (Wave 1 → 2 → 3)
- Some Wave 2/3 issues **depend on Wave 1**
- Use **acceptance criteria** as your checklist
- Each issue has **point values** for effort estimation
- **Total 39 points** = good-sized project

---

**Ready to start?** Pick your method above and create those issues! 🎯

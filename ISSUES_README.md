# GitHub Issues Creation Scripts

This directory contains scripts to create all GitHub issues for the ClassCrawler project as specified in the project requirements.

## Overview

The scripts will create 18 GitHub issues across 3 waves:
- **Wave 1**: 5 issues (foundational classes and CI setup)
- **Wave 2**: 8 issues (game logic and patterns)
- **Wave 3**: 5 issues (persistence, UI, and testing)

## Prerequisites

### Option 1: Using GitHub CLI (Recommended)
- Install [GitHub CLI](https://cli.github.com/)
- Authenticate: `gh auth login`

### Option 2: Using GitHub Token
- Create a Personal Access Token with `repo` scope
- Set environment variable: `export GITHUB_TOKEN=your_token_here`

## Usage

### Bash Script (Linux/Mac)
```bash
chmod +x create_issues.sh
./create_issues.sh
```

### Python Script (Cross-platform)
```bash
python3 create_issues.py
```

## Issue Structure

Each issue includes:
- Title with point value (e.g., "[2pts] Issue Title")
- Labels: wave number (wave-1, wave-2, wave-3) and difficulty (difficulty-1, difficulty-2, difficulty-3)
- Detailed description with:
  - Overview of the task
  - Required properties/methods/features
  - Dependencies on other issues (where applicable)
  - Acceptance criteria as a checklist

## Wave Breakdown

### Wave 1 - Foundation (9 points total)
1. **[2pts]** Create Character abstract base class
2. **[2pts]** Create Item abstract base class and subclasses
3. **[2pts]** Create Room and Dungeon classes
4. **[1pt]** Define IGameRepository interface
5. **[2pts]** Set up GitHub Actions CI pipeline

### Wave 2 - Game Logic (18 points total)
1. **[2pts]** Implement Player class
2. **[2pts]** Create Enemy abstract class and concrete enemy types
3. **[3pts]** Define ICombatStrategy interface and implement concrete strategies
4. **[2pts]** Implement CharacterFactory
5. **[3pts]** Implement GameEventSystem using Observer pattern
6. **[3pts]** Implement turn-based combat loop
7. **[2pts]** Implement loot system
8. **[2pts]** Implement player leveling and stat progression

### Wave 3 - Integration (12 points total)
1. **[3pts]** Implement SqliteGameRepository
2. **[2pts]** Add leaderboard feature
3. **[3pts]** Build console UI layer
4. **[2pts]** Write unit tests — combat system
5. **[2pts]** Write unit tests — items and inventory

**Total: 39 points across 18 issues**

## Troubleshooting

### Authentication Issues
If you encounter authentication errors:
1. Ensure you're authenticated with GitHub CLI: `gh auth status`
2. Or set your GitHub token: `export GITHUB_TOKEN=your_token`

### Rate Limiting
If you hit GitHub API rate limits:
- Wait a few minutes before retrying
- Authenticated requests have higher rate limits

### Partial Success
If some issues fail to create:
- Check the output to see which issues were created
- Re-run the script (it will attempt to create failed issues)
- Manually create remaining issues using the GitHub web interface

## Manual Creation

If automated creation fails, you can manually create issues using the content from the scripts. Each issue includes:
- Clear title with point value
- Appropriate labels (wave-X, difficulty-Y)
- Complete description with acceptance criteria

## Notes

- Issues are designed to be worked on in wave order (Wave 1 → Wave 2 → Wave 3)
- Some Wave 2 and Wave 3 issues have dependencies on Wave 1 issues
- Dependencies are noted in each issue description
- All issues include acceptance criteria as checklists for tracking progress

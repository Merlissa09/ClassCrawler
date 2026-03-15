# ClassCrawler

> A C# dungeon crawler where good object-oriented design is your best weapon.

## Overview

ClassCrawler is a turn-based dungeon crawler built with C# and .NET 8.
It is designed as a **teaching scaffold**: the architecture and interfaces are
fully defined, but the core method bodies are left unimplemented — your job is
to bring the game to life.

Work through the namespaces listed below, replace every `// TODO: Implement`
and `throw new NotImplementedException()` with working code, and watch the
test suite go green.

## Getting Started

```bash
# Clone the repository
git clone https://github.com/Merlissa09/ClassCrawler.git
cd ClassCrawler

# Run the application
dotnet run --project ClassCrawler
```

## Project Structure

```
ClassCrawler/
├── ClassCrawler/               # Main console application
│   ├── Characters/             # Character hierarchy (Player, Enemy, Goblin, Orc, Dragon)
│   ├── Items/                  # Item hierarchy (Weapon, Armor, Potion)
│   ├── Combat/                 # Combat strategies, engine, factory, loot resolver
│   ├── World/                  # Room and Dungeon classes
│   ├── Events/                 # Event system (publish / subscribe)
│   ├── Persistence/            # Save / load and leaderboard (SQLite)
│   ├── UI/                     # Console UI entry point
│   └── Program.cs
├── ClassCrawler.Tests/         # xUnit test project
│   ├── CombatEngineTests.cs
│   ├── CombatStrategyTests.cs
│   ├── ItemTests.cs
│   ├── InventoryTests.cs
│   └── LootResolverTests.cs
└── ClassCrawler.sln
```

## Creating Project Issues

This repository includes scripts to create all required GitHub issues for the project. The issues are organized into three waves:

- **Wave 1** (9 points): Foundation - Core classes and CI setup
- **Wave 2** (18 points): Game Logic - Combat, events, and patterns
- **Wave 3** (12 points): Integration - Persistence, UI, and tests

### Automated Creation

#### Option 1: Using GitHub Actions (Easiest)
1. Go to the "Actions" tab in your repository
2. Select "Create Project Issues" workflow
3. Click "Run workflow"
4. Choose which wave to create (or "all")

#### Option 2: Using Scripts
```bash
# Using bash script (Linux/Mac)
chmod +x create_issues.sh
./create_issues.sh

# OR using Python script (Cross-platform)
python3 create_issues.py
```

### Manual Creation

If automated methods don't work, follow the step-by-step instructions in `MANUAL_ISSUE_CREATION.md`.

For complete documentation, see `ISSUES_README.md`.

## Contributing

<!-- TODO: Add contribution guidelines -->

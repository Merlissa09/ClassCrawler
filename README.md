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

## Contributing

<!-- TODO: Add contribution guidelines -->

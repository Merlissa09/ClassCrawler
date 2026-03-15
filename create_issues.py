#!/usr/bin/env python3
"""
Script to create GitHub issues for ClassCrawler project.
This script creates all issues across Wave 1, Wave 2, and Wave 3.

Usage:
    python3 create_issues.py

Requires:
    - GitHub CLI (gh) installed and authenticated
    - Or set GITHUB_TOKEN environment variable for API access
"""

import subprocess
import sys

REPO = "Merlissa09/ClassCrawler"

def create_issue(title, labels, body):
    """Create a GitHub issue using gh CLI."""
    try:
        cmd = [
            "gh", "issue", "create",
            "--repo", REPO,
            "--title", title,
            "--label", labels,
            "--body", body
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✓ Created: {title}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to create: {title}")
        print(f"  Error: {e.stderr}")
        return False

def main():
    print("Creating GitHub issues for ClassCrawler...")
    print("=" * 50)
    print()

    issues_created = 0
    issues_failed = 0

    # Wave 1 Issues
    print("Creating Wave 1 issues...")
    
    wave1_issues = [
        {
            "title": "[2pts] Create Character abstract base class",
            "labels": "wave-1,difficulty-2",
            "body": """## Description
Create the abstract Character base class with the following properties and methods.

## Properties
- Name (string)
- Health (int)
- MaxHealth (int)
- AttackPower (int)
- Defense (int)
- Level (int)
- IsAlive (bool)

## Methods
- **abstract** TakeDamage(int amount)
- **virtual** GetDescription()

## Requirements
- Enforce that Health cannot go below 0
- Implement IsAlive property logic

## Acceptance Criteria
- [ ] Character abstract class is created with all required properties
- [ ] TakeDamage(int amount) abstract method is declared
- [ ] GetDescription() virtual method is implemented
- [ ] Health property enforces non-negative values (cannot go below 0)
- [ ] IsAlive property correctly reflects whether Health > 0
- [ ] Class is properly documented with XML comments"""
        },
        {
            "title": "[2pts] Create Item abstract base class and subclasses",
            "labels": "wave-1,difficulty-2",
            "body": """## Description
Create an abstract Item base class and concrete subclasses for Weapon, Armor, and Potion.

## Abstract Item Class Properties
- Name (string)
- Description (string)
- Weight (double)

## Abstract Item Class Methods
- **abstract** Use(Character target)
- **virtual** GetDescription()

## Concrete Subclasses

### Weapon
- DamageBonus (int)
- Override Use() to apply damage bonus
- Override GetDescription()

### Armor
- DefenseBonus (int)
- Override Use() to apply defense bonus
- Override GetDescription()

### Potion
- HealAmount (int)
- Override Use() to heal target
- Override GetDescription()

## Acceptance Criteria
- [ ] Abstract Item base class created with Name, Description, Weight properties
- [ ] Abstract Use(Character target) method declared
- [ ] Virtual GetDescription() method implemented
- [ ] Weapon subclass with DamageBonus property implemented
- [ ] Armor subclass with DefenseBonus property implemented
- [ ] Potion subclass with HealAmount property implemented
- [ ] Each subclass properly overrides Use() method
- [ ] Each subclass properly overrides GetDescription() method
- [ ] All classes documented with XML comments"""
        },
        {
            "title": "[2pts] Create Room and Dungeon classes",
            "labels": "wave-1,difficulty-2",
            "body": """## Description
Create Room and Dungeon classes for managing the game world structure.

## Room Class
### Properties
- Name (string)
- Description (string)
- Enemies (List<Enemy>)
- Items (List<Item>)
- IsCleared (bool)
- Exits (Dictionary<string, Room>)

## Dungeon Class
### Properties
- Rooms (List<Room>)
- CurrentRoom (Room)

### Methods
- MovePlayer(string direction) - moves player to adjacent room
- **static** GenerateDungeon() - creates a 4-room test dungeon

## Acceptance Criteria
- [ ] Room class created with all required properties
- [ ] Room.Exits dictionary allows connections between rooms
- [ ] Dungeon class created with Rooms and CurrentRoom properties
- [ ] MovePlayer(string direction) method implemented
- [ ] Static GenerateDungeon() method creates a 4-room test dungeon
- [ ] Test dungeon has proper room connections via Exits
- [ ] All classes documented with XML comments"""
        },
        {
            "title": "[1pt] Define IGameRepository interface",
            "labels": "wave-1,difficulty-1",
            "body": """## Description
Define the IGameRepository interface and GameState record for game persistence. This is interface and model definition only - no implementation required.

## IGameRepository Interface Methods
- SaveGame(GameState state)
- LoadGame(string playerName) returns GameState or null
- SaveScore(string playerName, int score)
- GetLeaderboard() returns List<LeaderboardEntry>

## GameState Record
A record type with the following properties:
- PlayerName (string)
- Health (int)
- Level (int)
- CurrentRoomName (string)
- Inventory (List<string>) - serialized item names

## LeaderboardEntry Record (if needed)
- PlayerName (string)
- Score (int)
- Date (DateTime)

## Acceptance Criteria
- [ ] IGameRepository interface defined with all required methods
- [ ] SaveGame(GameState) method signature declared
- [ ] LoadGame(string playerName) method signature declared
- [ ] SaveScore(string playerName, int score) method signature declared
- [ ] GetLeaderboard() method signature declared
- [ ] GameState record defined with all required properties
- [ ] All interfaces and records documented with XML comments
- [ ] No implementation code - interface definition only"""
        },
        {
            "title": "[2pts] Set up GitHub Actions CI pipeline",
            "labels": "wave-1,difficulty-2",
            "body": """## Description
Create a GitHub Actions workflow for continuous integration that builds and tests the project.

## Workflow Configuration
- File: .github/workflows/ci.yml
- Triggers: push to main branch and all pull requests
- .NET version: 8

## Workflow Steps
1. Checkout code
2. Setup .NET 8
3. Restore dependencies (dotnet restore)
4. Build project (dotnet build)
5. Run tests (dotnet test)

## Additional Requirements
- Add a passing build badge to README.md
- Badge should link to the workflow runs
- Badge format: ![Build Status](workflow-badge-url)

## Acceptance Criteria
- [ ] .github/workflows/ci.yml file created
- [ ] Workflow triggers on push to main branch
- [ ] Workflow triggers on all pull requests
- [ ] Checkout step included
- [ ] Setup .NET 8 step included
- [ ] dotnet restore step included
- [ ] dotnet build step included
- [ ] dotnet test step included
- [ ] Build badge added to README.md
- [ ] Badge correctly shows build status
- [ ] Workflow runs successfully on push"""
        }
    ]

    for issue in wave1_issues:
        if create_issue(issue["title"], issue["labels"], issue["body"]):
            issues_created += 1
        else:
            issues_failed += 1

    print()
    print("Wave 1 issues completed!")
    print()

    # Wave 2 Issues
    print("Creating Wave 2 issues...")
    
    wave2_issues = [
        {
            "title": "[2pts] Implement Player class",
            "labels": "wave-2,difficulty-2",
            "body": """## Description
Implement the Player class that inherits from Character base class.

**Depends on:** Character base class issue

## Additional Properties
- Inventory (List<Item>)
- Experience (int)
- Gold (int)

## Methods
- AddItem(Item item)
- RemoveItem(Item item)
- UseItem(Item item)
- AddExperience(int amount)
- Override GetDescription() to include inventory summary

## Requirements
- AddExperience should include a stub for triggering level-up
- Inventory operations should properly manage the item list
- GetDescription should show player stats and inventory summary

## Acceptance Criteria
- [ ] Player class inherits from Character
- [ ] Inventory property (List<Item>) implemented
- [ ] Experience property implemented
- [ ] Gold property implemented
- [ ] AddItem(Item item) method implemented
- [ ] RemoveItem(Item item) method implemented
- [ ] UseItem(Item item) method implemented
- [ ] AddExperience(int amount) method with level-up stub implemented
- [ ] GetDescription() overridden to include inventory summary
- [ ] Class documented with XML comments"""
        },
        {
            "title": "[2pts] Create Enemy abstract class and concrete enemy types",
            "labels": "wave-2,difficulty-2",
            "body": """## Description
Create abstract Enemy class and concrete enemy type implementations.

**Depends on:** Character base class issue

## Enemy Abstract Class
Inherits from Character and adds:
- ExperienceReward (int)
- GoldReward (int)
- LootTable (List<Item>)
- **abstract** GetAttackDescription() method

## Concrete Enemy Types

### Goblin
- Low stats (low health, attack, defense)
- Distinct flavor text in GetAttackDescription()

### Orc
- High health
- Medium attack and defense
- Distinct flavor text in GetAttackDescription()

### Dragon
- Boss tier stats (very high in all categories)
- Distinct flavor text in GetAttackDescription()

## Acceptance Criteria
- [ ] Enemy abstract class inherits from Character
- [ ] ExperienceReward property added
- [ ] GoldReward property added
- [ ] LootTable property (List<Item>) added
- [ ] Abstract GetAttackDescription() method declared
- [ ] Goblin concrete class implemented with low stats
- [ ] Orc concrete class implemented with high health
- [ ] Dragon concrete class implemented with boss-tier stats
- [ ] Each enemy type has distinct flavor text
- [ ] All classes documented with XML comments"""
        },
        {
            "title": "[3pts] Define ICombatStrategy interface and implement concrete strategies",
            "labels": "wave-2,difficulty-3",
            "body": """## Description
Implement the Strategy pattern for combat actions using ICombatStrategy interface.

**Depends on:** Character base class issue

## ICombatStrategy Interface
- Execute(Character attacker, Character target) returns CombatResult

## CombatResult Class
- DamageDealt (int)
- AttackerName (string)
- TargetName (string)
- Message (string)

## Concrete Strategy Implementations

### MeleeStrategy
- Direct physical damage calculation
- Uses attacker's AttackPower and target's Defense

### MagicStrategy
- Magic damage that partially bypasses defense
- Different calculation than melee

### RangedStrategy
- Ranged attack with different mechanics
- Unique damage calculation

## Integration
- Add CombatStrategy property to Character base class
- Include code comment explaining Strategy pattern choice

## Acceptance Criteria
- [ ] ICombatStrategy interface defined with Execute method
- [ ] CombatResult class created with all properties
- [ ] MeleeStrategy implemented
- [ ] MagicStrategy implemented
- [ ] RangedStrategy implemented
- [ ] Character.CombatStrategy property added
- [ ] Each strategy has distinct damage calculation
- [ ] Code comment explaining Strategy pattern included
- [ ] All classes and interfaces documented with XML comments"""
        },
        {
            "title": "[2pts] Implement CharacterFactory",
            "labels": "wave-2,difficulty-2",
            "body": """## Description
Implement a Factory pattern for creating Player and Enemy instances with preset configurations.

**Depends on:** Character and Enemy classes issues

## CharacterFactory Static Class

### CreatePlayer(string name, string characterClass)
Supports three character classes:
- **warrior**: High health and defense, MeleeStrategy
- **mage**: High attack power, low defense, MagicStrategy
- **rogue**: Balanced stats, RangedStrategy

### CreateEnemy(string type, int scalingLevel)
Creates enemies with scaled stats:
- **goblin**: Base stats scaled by level
- **orc**: Base stats scaled by level
- **dragon**: Base stats scaled by level

## Requirements
- Each character class has distinct stat distributions
- Each gets an appropriate default ICombatStrategy
- Enemy stats scale with level parameter
- Include code comment explaining Factory pattern choice

## Acceptance Criteria
- [ ] CharacterFactory static class created
- [ ] CreatePlayer(string name, string characterClass) implemented
- [ ] Warrior class configuration with MeleeStrategy
- [ ] Mage class configuration with MagicStrategy
- [ ] Rogue class configuration with RangedStrategy
- [ ] CreateEnemy(string type, int scalingLevel) implemented
- [ ] Goblin creation with stat scaling
- [ ] Orc creation with stat scaling
- [ ] Dragon creation with stat scaling
- [ ] Code comment explaining Factory pattern choice
- [ ] Class documented with XML comments"""
        },
        {
            "title": "[3pts] Implement GameEventSystem using Observer pattern",
            "labels": "wave-2,difficulty-3",
            "body": """## Description
Implement an event system using the Observer pattern for game-wide notifications.

## IGameEventListener Interface
- OnEvent(GameEvent gameEvent)

## GameEvent Abstract Base Class
- EventType (enum)
- Message (string)
- Timestamp (DateTime)

## EventType Enum
- PlayerLevelUp
- EnemyDefeated
- ItemPickedUp
- PlayerDeath

## Concrete Event Classes
- PlayerLevelUpEvent (includes new level)
- EnemyDefeatedEvent (includes enemy name, XP, gold)
- ItemPickedUpEvent (includes item name)
- PlayerDeathEvent (includes cause of death)

## GameEventSystem Static Class
- Subscribe(IGameEventListener listener)
- Unsubscribe(IGameEventListener listener)
- Publish(GameEvent gameEvent)

## Demo Implementation
- GameLogger class implements IGameEventListener
- Prints events to console with formatting

## Requirements
- Include code comment explaining Observer pattern choice
- Thread-safe implementation (not required if single-threaded)

## Acceptance Criteria
- [ ] IGameEventListener interface defined
- [ ] GameEvent abstract base class created
- [ ] EventType enum defined
- [ ] PlayerLevelUpEvent implemented
- [ ] EnemyDefeatedEvent implemented
- [ ] ItemPickedUpEvent implemented
- [ ] PlayerDeathEvent implemented
- [ ] GameEventSystem static class with Subscribe/Unsubscribe/Publish
- [ ] GameLogger demo listener implemented
- [ ] Code comment explaining Observer pattern choice
- [ ] All classes documented with XML comments"""
        },
        {
            "title": "[3pts] Implement turn-based combat loop",
            "labels": "wave-2,difficulty-3",
            "body": """## Description
Implement turn-based combat system with CombatEngine class.

**Depends on:** Character, Player, Enemy, and ICombatStrategy issues

## CombatEngine Class

### RunCombat(Player player, Enemy enemy)
Returns CombatOutcome with:
- Winner (Character)
- TotalDamageDealt (int)
- ExperienceEarned (int)
- GoldEarned (int)
- TurnCount (int)

## Combat Rules
- Player attacks first each turn
- Each character uses their ICombatStrategy.Execute()
- Combat continues until one character dies (Health <= 0)
- Publishes events via GameEventSystem:
  - EnemyDefeatedEvent if player wins
  - PlayerDeathEvent if enemy wins

## Requirements
- No UI/console output in CombatEngine
- Pure game logic only
- Combat result encapsulates all outcome data

## Acceptance Criteria
- [ ] CombatEngine class created
- [ ] RunCombat(Player player, Enemy enemy) method implemented
- [ ] CombatOutcome class defined with all properties
- [ ] Player attacks first each turn
- [ ] Uses ICombatStrategy.Execute() for attacks
- [ ] Combat continues until one character's Health <= 0
- [ ] Publishes EnemyDefeatedEvent on enemy death
- [ ] Publishes PlayerDeathEvent on player death
- [ ] Returns complete CombatOutcome
- [ ] No UI logic in class
- [ ] Class documented with XML comments"""
        },
        {
            "title": "[2pts] Implement loot system",
            "labels": "wave-2,difficulty-2",
            "body": """## Description
Implement loot generation system with configurable drop rates.

**Depends on:** Enemy and Item classes issues

## LootResolver Class

### ResolveLoot(Enemy enemy)
Returns List<Item> based on:
- Enemy's LootTable
- Configurable drop probability per item
- Special rules for boss enemies

## Loot Rules
- Each item in LootTable has a drop probability (0.0 - 1.0)
- Dragon always drops at least one item
- Gold always equals enemy.GoldReward
- Random seed should be injectable for deterministic testing

## Requirements
- Constructor accepts optional Random seed for testing
- Default uses unseeded Random for production
- Item drop rates are configurable per item

## Acceptance Criteria
- [ ] LootResolver class created
- [ ] ResolveLoot(Enemy enemy) method implemented
- [ ] Returns List<Item> based on LootTable
- [ ] Supports configurable drop probability per item
- [ ] Dragon always drops at least one item
- [ ] Gold amount equals enemy.GoldReward
- [ ] Constructor accepts optional Random seed
- [ ] Deterministic loot generation with seed for testing
- [ ] Default random behavior for production
- [ ] Class documented with XML comments"""
        },
        {
            "title": "[2pts] Implement player leveling and stat progression",
            "labels": "wave-2,difficulty-2",
            "body": """## Description
Implement player leveling system with XP thresholds and stat progression.

**Depends on:** Player class issue

## Level System
- Define XP thresholds for levels 1-10
- Example: Level 2 = 100 XP, Level 3 = 250 XP, etc.

## Level Up Effects
When player levels up:
- Increment Level property
- Increase AttackPower (e.g., +2)
- Increase Defense (e.g., +1)
- Increase MaxHealth (e.g., +10)
- Restore some Health (e.g., 50% of MaxHealth)
- Publish PlayerLevelUpEvent via GameEventSystem

## Progress Tracking
- GetProgressToNextLevel() method
- Returns double (0.0 - 1.0) representing progress
- Used for UI progress bars

## Acceptance Criteria
- [ ] XP thresholds defined for levels 1-10
- [ ] Level up logic implemented in Player.AddExperience()
- [ ] AttackPower increases on level up
- [ ] Defense increases on level up
- [ ] MaxHealth increases on level up
- [ ] Health restored partially on level up
- [ ] PlayerLevelUpEvent published via GameEventSystem
- [ ] GetProgressToNextLevel() method implemented
- [ ] Returns 0.0 - 1.0 progress value
- [ ] Method documented with XML comments"""
        }
    ]

    for issue in wave2_issues:
        if create_issue(issue["title"], issue["labels"], issue["body"]):
            issues_created += 1
        else:
            issues_failed += 1

    print()
    print("Wave 2 issues completed!")
    print()

    # Wave 3 Issues
    print("Creating Wave 3 issues...")
    
    wave3_issues = [
        {
            "title": "[3pts] Implement SqliteGameRepository",
            "labels": "wave-3,difficulty-3",
            "body": """## Description
Implement IGameRepository interface using SQLite database for persistence.

**Depends on:** IGameRepository interface issue

## SqliteGameRepository Class
Implements IGameRepository using Microsoft.Data.Sqlite

## Database Operations

### SaveGame(GameState state)
- Upserts game save by player name
- Creates tables if they don't exist

### LoadGame(string playerName)
- Returns GameState if found
- Returns null if not found

### SaveScore(string playerName, int score)
- Inserts new leaderboard entry
- Includes timestamp

### GetLeaderboard()
- Returns top 10 scores
- Ordered by score descending
- Includes player name, score, and date

## Requirements
- Creates database and tables on first run
- Use 'using' statements for connection disposal
- Proper SQL parameterization to prevent injection
- Database file: classcrawler.db

## Acceptance Criteria
- [ ] SqliteGameRepository class implements IGameRepository
- [ ] Uses Microsoft.Data.Sqlite package
- [ ] Creates database and tables on first run
- [ ] SaveGame(GameState) upserts by player name
- [ ] LoadGame(string playerName) returns GameState or null
- [ ] SaveScore(string playerName, int score) inserts with timestamp
- [ ] GetLeaderboard() returns top 10 scores descending
- [ ] Uses 'using' statements for proper disposal
- [ ] SQL uses parameters (no injection vulnerabilities)
- [ ] Class documented with XML comments"""
        },
        {
            "title": "[2pts] Add leaderboard feature",
            "labels": "wave-3,difficulty-2",
            "body": """## Description
Implement score calculation and leaderboard display functionality.

**Depends on:** SqliteGameRepository issue

## Score Calculation
Calculate final score based on:
- Enemies defeated (points per enemy)
- Gold collected
- Level reached
- Bonus multipliers for difficulty

## Leaderboard Display
- Show top 10 scores
- Display: rank, player name, score, date
- Accessible from main menu
- Friendly message if no scores exist

## Integration
- Save score via IGameRepository.SaveScore() at game end
- Retrieve scores via IGameRepository.GetLeaderboard()

## Acceptance Criteria
- [ ] Score calculation implemented based on metrics
- [ ] Considers enemies defeated
- [ ] Considers gold collected
- [ ] Considers level reached
- [ ] Score saved via IGameRepository.SaveScore() at game end
- [ ] Leaderboard accessible from main menu
- [ ] Displays top 10 scores
- [ ] Shows rank, name, score, and date
- [ ] Friendly message shown if no scores exist
- [ ] Properly formatted display output"""
        },
        {
            "title": "[3pts] Build console UI layer",
            "labels": "wave-3,difficulty-3",
            "body": """## Description
Create console-based user interface for the game.

**Depends on:** Player, Dungeon, and CombatEngine issues

## GameUI Class
Static Run() method as entry point

## Main Menu Options
- New Game
- Load Game
- Leaderboard
- Quit

## Room View
Display:
- Room name and description
- Available exits
- Enemies present
- Items on ground

## Player Actions
- Move (north, south, east, west)
- Attack enemy
- Pick up item
- Use item
- View stats/inventory

## Combat Display
- Show turn-by-turn results
- Display damage dealt
- Show health changes
- Announce winner

## Game Over Screen
- Display final stats
- Save score to leaderboard
- Option to return to main menu

## Requirements
- No game logic in UI layer
- Call game methods and display results only
- Clear separation of concerns
- User-friendly prompts and output

## Acceptance Criteria
- [ ] GameUI class with static Run() entry point
- [ ] Main menu with all options implemented
- [ ] New Game starts new player
- [ ] Load Game retrieves saved game
- [ ] Leaderboard displays top scores
- [ ] Quit exits gracefully
- [ ] Room view shows all required information
- [ ] Player can move between rooms
- [ ] Player can attack enemies
- [ ] Player can pick up items
- [ ] Player can use items
- [ ] Player can view stats
- [ ] Combat output shows turn details
- [ ] Game over screen saves score
- [ ] No game logic in UI - only display
- [ ] User-friendly prompts and formatting"""
        },
        {
            "title": "[2pts] Write unit tests — combat system",
            "labels": "wave-3,difficulty-2",
            "body": """## Description
Create comprehensive unit tests for combat system components.

**Depends on:** ICombatStrategy and CombatEngine issues

## Test Coverage

### ICombatStrategy Tests
- Test each strategy (Melee, Magic, Ranged)
- Verify damage calculation formulas
- Test with various attack and defense values
- Test edge cases

### CombatEngine Tests
- Test RunCombat() method
- Player wins scenario
- Enemy wins scenario
- Verify correct XP returned
- Verify correct Gold returned
- Test turn order (player attacks first)

## Edge Cases to Cover
- Zero health
- Maximum defense (damage reduction)
- Zero attack power
- Negative values (should not occur)

## Requirements
- Use xUnit testing framework
- Use seeded Random for deterministic tests
- All tests must pass in CI pipeline
- Good test naming conventions

## Acceptance Criteria
- [ ] Test class for ICombatStrategy implementations
- [ ] MeleeStrategy damage calculation tested
- [ ] MagicStrategy damage calculation tested
- [ ] RangedStrategy damage calculation tested
- [ ] Test class for CombatEngine
- [ ] Player wins scenario tested
- [ ] Enemy wins scenario tested
- [ ] XP reward calculation tested
- [ ] Gold reward calculation tested
- [ ] Turn order verified
- [ ] Edge cases tested (zero health, max defense, zero attack)
- [ ] Uses seeded Random for deterministic behavior
- [ ] All tests pass in CI
- [ ] Tests follow naming conventions"""
        },
        {
            "title": "[2pts] Write unit tests — items and inventory",
            "labels": "wave-3,difficulty-2",
            "body": """## Description
Create comprehensive unit tests for item system and player inventory.

**Depends on:** Item subclasses and Player issues

## Test Coverage

### Item Subclass Tests
- **Weapon.Use()**: Verify damage bonus applied correctly
- **Armor.Use()**: Verify defense bonus applied correctly
- **Potion.Use()**: Verify healing applied correctly
- Potion healing capped at MaxHealth

### Player Inventory Tests
- AddItem() adds item to inventory
- RemoveItem() removes item from inventory
- UseItem() applies item effect and removes from inventory
- Inventory state changes verified

### LootResolver Tests
- Test with injected seed for deterministic drops
- Verify drop probability calculations
- Verify Dragon always drops at least one item
- Verify Gold equals GoldReward

## Requirements
- Use xUnit testing framework
- Use seeded Random for loot tests
- Test edge cases (full health, empty inventory, etc.)
- All tests must pass in CI pipeline

## Acceptance Criteria
- [ ] Test class for Item subclasses
- [ ] Weapon.Use() damage bonus tested
- [ ] Armor.Use() defense bonus tested
- [ ] Potion.Use() healing tested
- [ ] Potion healing capped at MaxHealth verified
- [ ] Test class for Player inventory operations
- [ ] AddItem() tested
- [ ] RemoveItem() tested
- [ ] UseItem() tested
- [ ] Inventory state changes verified
- [ ] Test class for LootResolver
- [ ] Tested with injected seed
- [ ] Drop probability logic verified
- [ ] Dragon loot guarantee tested
- [ ] Gold amount verification tested
- [ ] All tests pass in CI
- [ ] Tests follow naming conventions"""
        }
    ]

    for issue in wave3_issues:
        if create_issue(issue["title"], issue["labels"], issue["body"]):
            issues_created += 1
        else:
            issues_failed += 1

    print()
    print("Wave 3 issues completed!")
    print()
    print("=" * 50)
    print(f"Summary: {issues_created} issues created successfully")
    if issues_failed > 0:
        print(f"         {issues_failed} issues failed")
    print("=" * 50)

    return 0 if issues_failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())

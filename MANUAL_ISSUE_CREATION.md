# Manual GitHub Issues Creation Guide

Since automated issue creation requires elevated GitHub permissions, please follow these instructions to manually create all issues for the ClassCrawler project.

## Quick Setup

You have two options:

### Option 1: Use the Automated Scripts (Recommended if you have gh CLI access)

1. **Install and authenticate GitHub CLI** (if not already done):
   ```bash
   # Install gh CLI (see https://cli.github.com/)
   gh auth login
   ```

2. **Run the script**:
   ```bash
   # Using bash script
   ./create_issues.sh
   
   # OR using Python script
   python3 create_issues.py
   ```

### Option 2: Create Issues Manually via GitHub Web Interface

Follow the detailed instructions below to create each issue one by one.

---

## Wave 1 Issues (5 issues - 9 points total)

### Issue 1: [2pts] Create Character abstract base class

**Labels**: `wave-1`, `difficulty-2`

**Description**:
```markdown
## Description
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
- [ ] Class is properly documented with XML comments
```

---

### Issue 2: [2pts] Create Item abstract base class and subclasses

**Labels**: `wave-1`, `difficulty-2`

**Description**:
```markdown
## Description
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
- [ ] All classes documented with XML comments
```

---

### Issue 3: [2pts] Create Room and Dungeon classes

**Labels**: `wave-1`, `difficulty-2`

**Description**:
```markdown
## Description
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
- [ ] All classes documented with XML comments
```

---

### Issue 4: [1pt] Define IGameRepository interface

**Labels**: `wave-1`, `difficulty-1`

**Description**:
```markdown
## Description
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
- [ ] No implementation code - interface definition only
```

---

### Issue 5: [2pts] Set up GitHub Actions CI pipeline

**Labels**: `wave-1`, `difficulty-2`

**Description**:
```markdown
## Description
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
- [ ] Workflow runs successfully on push
```

---

## Wave 2 Issues (8 issues - 18 points total)

For Wave 2 issues, please refer to the `create_issues.sh` or `create_issues.py` scripts which contain all the detailed descriptions. The titles are:

1. **[2pts] Implement Player class** (wave-2, difficulty-2)
2. **[2pts] Create Enemy abstract class and concrete enemy types** (wave-2, difficulty-2)
3. **[3pts] Define ICombatStrategy interface and implement concrete strategies** (wave-2, difficulty-3)
4. **[2pts] Implement CharacterFactory** (wave-2, difficulty-2)
5. **[3pts] Implement GameEventSystem using Observer pattern** (wave-2, difficulty-3)
6. **[3pts] Implement turn-based combat loop** (wave-2, difficulty-3)
7. **[2pts] Implement loot system** (wave-2, difficulty-2)
8. **[2pts] Implement player leveling and stat progression** (wave-2, difficulty-2)

---

## Wave 3 Issues (5 issues - 12 points total)

For Wave 3 issues, please refer to the `create_issues.sh` or `create_issues.py` scripts which contain all the detailed descriptions. The titles are:

1. **[3pts] Implement SqliteGameRepository** (wave-3, difficulty-3)
2. **[2pts] Add leaderboard feature** (wave-3, difficulty-2)
3. **[3pts] Build console UI layer** (wave-3, difficulty-3)
4. **[2pts] Write unit tests — combat system** (wave-3, difficulty-2)
5. **[2pts] Write unit tests — items and inventory** (wave-3, difficulty-2)

---

## How to Create Issues via GitHub Web Interface

1. Go to your repository: https://github.com/Merlissa09/ClassCrawler
2. Click on the "Issues" tab
3. Click the green "New issue" button
4. Copy the title from above (e.g., `[2pts] Create Character abstract base class`)
5. Copy the description from above
6. Add labels on the right side:
   - Add the wave label (e.g., `wave-1`)
   - Add the difficulty label (e.g., `difficulty-2`)
7. Click "Submit new issue"
8. Repeat for all 18 issues

---

## Creating Labels (if they don't exist)

If the labels don't exist yet, create them first:

1. Go to Issues → Labels
2. Click "New label"
3. Create these labels:
   - `wave-1` (color: #0E8A16 - green)
   - `wave-2` (color: #FBCA04 - yellow)
   - `wave-3` (color: #D93F0B - red)
   - `difficulty-1` (color: #C5DEF5 - light blue)
   - `difficulty-2` (color: #5319E7 - purple)
   - `difficulty-3` (color: #B60205 - dark red)

---

## Tips

- Create issues in order (Wave 1 → Wave 2 → Wave 3) as some have dependencies
- Use the checklist in each issue's acceptance criteria to track progress
- The full issue descriptions are available in `create_issues.sh` and `create_issues.py`
- Consider creating a GitHub Project board to organize and track these issues

---

## Total Points

- **Wave 1**: 9 points
- **Wave 2**: 18 points
- **Wave 3**: 12 points
- **Total**: 39 points across 18 issues

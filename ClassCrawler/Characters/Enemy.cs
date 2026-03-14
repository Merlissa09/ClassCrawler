using ClassCrawler.Items;

namespace ClassCrawler.Characters;

/// <summary>Abstract base class for all enemy characters.</summary>
public abstract class Enemy : Character
{
    /// <summary>The amount of experience awarded to the player upon defeating this enemy.</summary>
    public int ExperienceReward { get; set; }

    /// <summary>The amount of gold awarded to the player upon defeating this enemy.</summary>
    public int GoldReward { get; set; }

    /// <summary>Items that may be dropped by this enemy when defeated.</summary>
    public List<Item> LootTable { get; set; } = new();

    /// <summary>Returns a description of this enemy's attack action.</summary>
    public abstract string GetAttackDescription();
}

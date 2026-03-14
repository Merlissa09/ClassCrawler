using ClassCrawler.Characters;

namespace ClassCrawler.Items;

/// <summary>Abstract base class for all items in the game.</summary>
public abstract class Item
{
    /// <summary>The item's display name.</summary>
    public string Name { get; set; } = string.Empty;

    /// <summary>A short description of the item.</summary>
    public string Description { get; set; } = string.Empty;

    /// <summary>The weight of the item in the player's inventory.</summary>
    public int Weight { get; set; }

    /// <summary>Applies this item's effect to the target character.</summary>
    public abstract void Use(Character target);
}

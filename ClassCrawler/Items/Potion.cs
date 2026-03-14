using ClassCrawler.Characters;

namespace ClassCrawler.Items;

/// <summary>A consumable potion that restores health to the target character.</summary>
public class Potion : Item
{
    /// <summary>The number of health points restored when this potion is used.</summary>
    public int HealAmount { get; set; }

    /// <summary>Drinks this potion, restoring health to the target character.</summary>
    public override void Use(Character target)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }
}

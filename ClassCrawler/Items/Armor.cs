using ClassCrawler.Characters;

namespace ClassCrawler.Items;

/// <summary>Armor that increases the wearer's defense.</summary>
public class Armor : Item
{
    /// <summary>The bonus added to the character's defense stat.</summary>
    public int DefenseBonus { get; set; }

    /// <summary>Equips this armor, applying its defense bonus to the target.</summary>
    public override void Use(Character target)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }
}

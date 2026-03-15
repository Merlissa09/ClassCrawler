using ClassCrawler.Characters;

namespace ClassCrawler.Items;

/// <summary>A weapon that increases the wielder's attack power.</summary>
public class Weapon : Item
{
    /// <summary>The bonus damage added to the character's attack power.</summary>
    public int DamageBonus { get; set; }

    /// <summary>Equips this weapon, applying its damage bonus to the target.</summary>
    public override void Use(Character target)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }
}

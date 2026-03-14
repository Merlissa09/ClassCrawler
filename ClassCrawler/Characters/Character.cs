using ClassCrawler.Combat;

namespace ClassCrawler.Characters;

/// <summary>Abstract base class for all characters in the game.</summary>
public abstract class Character
{
    /// <summary>The character's display name.</summary>
    public string Name { get; set; } = string.Empty;

    /// <summary>The character's current health points.</summary>
    public int Health { get; set; }

    /// <summary>The character's maximum health points.</summary>
    public int MaxHealth { get; set; }

    /// <summary>The base damage this character deals per attack.</summary>
    public int AttackPower { get; set; }

    /// <summary>Reduces incoming damage by this amount.</summary>
    public int Defense { get; set; }

    /// <summary>The character's current level.</summary>
    public int Level { get; set; }

    /// <summary>Indicates whether the character is still alive.</summary>
    public bool IsAlive => Health > 0;

    /// <summary>The combat strategy used when this character attacks.</summary>
    public ICombatStrategy? CombatStrategy { get; set; }

    /// <summary>Applies damage to this character.</summary>
    public abstract void TakeDamage(int amount);

    /// <summary>Returns a human-readable description of this character.</summary>
    public virtual string GetDescription()
    {
        // TODO: Implement
        throw new NotImplementedException();
    }
}

namespace ClassCrawler.Characters;

/// <summary>A fearsome dragon — the ultimate dungeon boss.</summary>
public class Dragon : Enemy
{
    /// <summary>Initialises a Dragon with default starting stats.</summary>
    public Dragon()
    {
        Name = "Dragon";
        Health = 200;
        MaxHealth = 200;
        AttackPower = 35;
        Defense = 15;
        Level = 10;
        ExperienceReward = 200;
        GoldReward = 100;
    }

    /// <summary>Returns a description of the Dragon's attack.</summary>
    public override string GetAttackDescription()
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Applies damage to the Dragon, reducing its health.</summary>
    public override void TakeDamage(int amount)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }
}

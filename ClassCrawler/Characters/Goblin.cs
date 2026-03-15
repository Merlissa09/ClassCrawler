namespace ClassCrawler.Characters;

/// <summary>A weak but cunning enemy found in early dungeon rooms.</summary>
public class Goblin : Enemy
{
    /// <summary>Initialises a Goblin with default starting stats.</summary>
    public Goblin()
    {
        Name = "Goblin";
        Health = 30;
        MaxHealth = 30;
        AttackPower = 5;
        Defense = 2;
        Level = 1;
        ExperienceReward = 10;
        GoldReward = 5;
    }

    /// <summary>Returns a description of the Goblin's attack.</summary>
    public override string GetAttackDescription()
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Applies damage to the Goblin, reducing its health.</summary>
    public override void TakeDamage(int amount)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }
}

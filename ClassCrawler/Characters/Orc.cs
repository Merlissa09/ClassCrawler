namespace ClassCrawler.Characters;

/// <summary>A brutish enemy with high health and strong attacks.</summary>
public class Orc : Enemy
{
    /// <summary>Initialises an Orc with default starting stats.</summary>
    public Orc()
    {
        Name = "Orc";
        Health = 60;
        MaxHealth = 60;
        AttackPower = 12;
        Defense = 5;
        Level = 3;
        ExperienceReward = 25;
        GoldReward = 15;
    }

    /// <summary>Returns a description of the Orc's attack.</summary>
    public override string GetAttackDescription()
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Applies damage to the Orc, reducing its health.</summary>
    public override void TakeDamage(int amount)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }
}

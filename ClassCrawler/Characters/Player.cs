using ClassCrawler.Items;

namespace ClassCrawler.Characters;

/// <summary>Represents the player character controlled by the user.</summary>
public class Player : Character
{
    /// <summary>The items currently carried by the player.</summary>
    public List<Item> Inventory { get; set; } = new();

    /// <summary>The total experience points earned by the player.</summary>
    public int Experience { get; set; }

    /// <summary>The amount of gold the player is carrying.</summary>
    public int Gold { get; set; }

    /// <summary>Adds an item to the player's inventory.</summary>
    public void AddItem(Item item)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Removes an item from the player's inventory.</summary>
    public void RemoveItem(Item item)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Uses an item from the player's inventory on this player.</summary>
    public void UseItem(Item item)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Adds experience points and checks for level-up.</summary>
    public void AddExperience(int amount)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Applies damage to the player, reducing their health.</summary>
    public override void TakeDamage(int amount)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }
}

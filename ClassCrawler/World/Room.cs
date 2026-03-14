using ClassCrawler.Characters;
using ClassCrawler.Items;

namespace ClassCrawler.World;

/// <summary>Represents a single room within the dungeon.</summary>
public class Room
{
    /// <summary>The name of this room.</summary>
    public string Name { get; set; } = string.Empty;

    /// <summary>A description of this room's appearance.</summary>
    public string Description { get; set; } = string.Empty;

    /// <summary>Enemies currently present in this room.</summary>
    public List<Enemy> Enemies { get; set; } = new();

    /// <summary>Items left on the floor of this room.</summary>
    public List<Item> Items { get; set; } = new();

    /// <summary>Indicates whether all enemies in this room have been defeated.</summary>
    public bool IsCleared { get; set; }

    /// <summary>Maps compass directions to adjacent rooms.</summary>
    public Dictionary<string, Room> Exits { get; set; } = new();
}

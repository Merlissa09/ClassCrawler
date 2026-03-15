namespace ClassCrawler.World;

/// <summary>Represents the entire dungeon and tracks the player's current location.</summary>
public class Dungeon
{
    /// <summary>All rooms that make up this dungeon.</summary>
    public List<Room> Rooms { get; set; } = new();

    /// <summary>The room the player is currently in.</summary>
    public Room? CurrentRoom { get; set; }

    /// <summary>Attempts to move the player in the given direction.</summary>
    public bool MovePlayer(string direction)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Creates a small four-room test dungeon and returns it.</summary>
    public static Dungeon GenerateDungeon()
    {
        // TODO: Implement
        throw new NotImplementedException();
    }
}

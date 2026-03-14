namespace ClassCrawler.Persistence;

/// <summary>A serializable snapshot of the current game state.</summary>
public record GameState(
    string PlayerName,
    int Health,
    int Level,
    string CurrentRoomName,
    List<string> Inventory);

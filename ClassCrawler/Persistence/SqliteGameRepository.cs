namespace ClassCrawler.Persistence;

/// <summary>SQLite-backed implementation of IGameRepository.</summary>
public class SqliteGameRepository : IGameRepository
{
    /// <summary>Persists the provided game state to the SQLite database.</summary>
    public void SaveGame(GameState gameState)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Loads a previously saved game state from the SQLite database.</summary>
    public GameState? LoadGame(string playerName)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Records a player's score in the SQLite leaderboard table.</summary>
    public void SaveScore(string playerName, int score)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Returns all leaderboard entries from the SQLite database.</summary>
    public List<LeaderboardEntry> GetLeaderboard()
    {
        // TODO: Implement
        throw new NotImplementedException();
    }
}

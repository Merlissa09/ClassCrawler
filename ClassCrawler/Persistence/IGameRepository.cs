namespace ClassCrawler.Persistence;

/// <summary>Defines the contract for persisting and retrieving game data.</summary>
public interface IGameRepository
{
    /// <summary>Persists the provided game state to storage.</summary>
    void SaveGame(GameState gameState);

    /// <summary>Loads a previously saved game state by player name.</summary>
    GameState? LoadGame(string playerName);

    /// <summary>Records a player's score on the leaderboard.</summary>
    void SaveScore(string playerName, int score);

    /// <summary>Returns all leaderboard entries ordered by score descending.</summary>
    List<LeaderboardEntry> GetLeaderboard();
}

namespace ClassCrawler.Persistence;

/// <summary>A single entry in the game leaderboard.</summary>
public record LeaderboardEntry(string PlayerName, int Score, DateTime DateAchieved);

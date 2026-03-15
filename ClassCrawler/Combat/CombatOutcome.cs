namespace ClassCrawler.Combat;

/// <summary>Represents the overall outcome of a completed combat encounter.</summary>
public record CombatOutcome(string Winner, int TotalDamageDealt, int ExperienceEarned, int GoldEarned);

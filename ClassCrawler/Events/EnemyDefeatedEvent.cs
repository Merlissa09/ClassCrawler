namespace ClassCrawler.Events;

/// <summary>Event raised when an enemy is defeated in combat.</summary>
public class EnemyDefeatedEvent : GameEvent
{
    /// <summary>Initialises an EnemyDefeatedEvent with a default message.</summary>
    public EnemyDefeatedEvent(string message)
        : base(GameEventType.EnemyDefeated, message) { }
}

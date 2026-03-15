namespace ClassCrawler.Events;

/// <summary>Event raised when the player's health reaches zero.</summary>
public class PlayerDeathEvent : GameEvent
{
    /// <summary>Initialises a PlayerDeathEvent with a default message.</summary>
    public PlayerDeathEvent(string message)
        : base(GameEventType.PlayerDeath, message) { }
}

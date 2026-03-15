namespace ClassCrawler.Events;

/// <summary>Event raised when the player gains a level.</summary>
public class PlayerLevelUpEvent : GameEvent
{
    /// <summary>Initialises a PlayerLevelUpEvent with a default message.</summary>
    public PlayerLevelUpEvent(string message)
        : base(GameEventType.PlayerLevelUp, message) { }
}

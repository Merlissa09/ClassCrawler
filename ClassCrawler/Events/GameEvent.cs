namespace ClassCrawler.Events;

/// <summary>Abstract base class for all game events.</summary>
public abstract class GameEvent
{
    /// <summary>The category of this event.</summary>
    public GameEventType EventType { get; }

    /// <summary>A human-readable message describing what happened.</summary>
    public string Message { get; }

    /// <summary>Initialises a new GameEvent with the given type and message.</summary>
    protected GameEvent(GameEventType eventType, string message)
    {
        EventType = eventType;
        Message = message;
    }
}

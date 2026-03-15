namespace ClassCrawler.Events;

/// <summary>Event raised when the player picks up an item.</summary>
public class ItemPickedUpEvent : GameEvent
{
    /// <summary>Initialises an ItemPickedUpEvent with a default message.</summary>
    public ItemPickedUpEvent(string message)
        : base(GameEventType.ItemPickedUp, message) { }
}

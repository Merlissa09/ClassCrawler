namespace ClassCrawler.Events;

/// <summary>Defines a listener that can receive and react to game events.</summary>
public interface IGameEventListener
{
    /// <summary>Called whenever a game event is published to the event system.</summary>
    void OnEvent(GameEvent gameEvent);
}

namespace ClassCrawler.Events;

/// <summary>Global publish/subscribe system for game events.</summary>
public static class GameEventSystem
{
    /// <summary>Registers a listener to receive future events.</summary>
    public static void Subscribe(IGameEventListener listener)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Removes a previously registered listener.</summary>
    public static void Unsubscribe(IGameEventListener listener)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }

    /// <summary>Broadcasts a game event to all registered listeners.</summary>
    public static void Publish(GameEvent gameEvent)
    {
        // TODO: Implement
        throw new NotImplementedException();
    }
}

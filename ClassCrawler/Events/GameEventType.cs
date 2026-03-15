namespace ClassCrawler.Events;

/// <summary>Categorises the types of events that can occur during gameplay.</summary>
public enum GameEventType
{
    /// <summary>Fired when the player gains enough experience to level up.</summary>
    PlayerLevelUp,

    /// <summary>Fired when an enemy is defeated in combat.</summary>
    EnemyDefeated,

    /// <summary>Fired when the player picks up an item.</summary>
    ItemPickedUp,

    /// <summary>Fired when the player's health reaches zero.</summary>
    PlayerDeath
}

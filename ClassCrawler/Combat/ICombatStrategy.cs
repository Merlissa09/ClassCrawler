using ClassCrawler.Characters;

namespace ClassCrawler.Combat;

/// <summary>Defines a strategy for executing a combat action between two characters.</summary>
public interface ICombatStrategy
{
    /// <summary>Executes the combat action from attacker to target and returns the result.</summary>
    CombatResult Execute(Character attacker, Character target);
}

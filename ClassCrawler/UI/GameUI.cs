namespace ClassCrawler.UI;

/// <summary>Manages all console-based user interaction for the game.</summary>
public class GameUI
{
    /// <summary>Entry point that starts the game and displays the main menu.</summary>
    public static void Run()
    {
        Console.WriteLine("Welcome to ClassCrawler!");

        bool running = true;
        while (running)
        {
            Console.WriteLine();
            Console.WriteLine("1. New Game");
            Console.WriteLine("2. Load Game");
            Console.WriteLine("3. Leaderboard");
            Console.WriteLine("4. Quit");
            Console.Write("> ");

            string? input = Console.ReadLine();
            switch (input)
            {
                case "1":
                    // TODO: Implement New Game
                    throw new NotImplementedException();
                case "2":
                    // TODO: Implement Load Game
                    throw new NotImplementedException();
                case "3":
                    // TODO: Implement Leaderboard
                    throw new NotImplementedException();
                case "4":
                    running = false;
                    break;
                default:
                    Console.WriteLine("Invalid option. Please try again.");
                    break;
            }
        }
    }
}

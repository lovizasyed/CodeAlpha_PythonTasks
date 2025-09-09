import random


def display_hangman(wrong_guesses):
    """Display hangman drawing based on number of wrong guesses"""
    stages = [
        """
           ------
           |    |
           |    
           |    
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |    
        --------
        """
    ]
    return stages[wrong_guesses]


def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed"""
    display = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def hangman_game():
    """Main hangman game function"""
    # Predefined list of words
    words = ["python", "programming", "computer", "keyboard", "monitor"]

    # Select random word
    word = random.choice(words).lower()

    # Initialize game variables
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("🎮 Welcome to Hangman Game! 🎮")
    print("Guess the word one letter at a time!")
    print(f"The word has {len(word)} letters.")
    print()

    # Main game loop
    while wrong_guesses < max_wrong_guesses:
        # Display current state
        print(display_hangman(wrong_guesses))
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Wrong guesses remaining: {max_wrong_guesses - wrong_guesses}")
        print()

        # Check if word is completely guessed
        if all(letter in guessed_letters for letter in word):
            print("🎉 Congratulations! You guessed the word!")
            print(f"The word was: {word.upper()}")
            return

        # Get user input
        guess = input("Enter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter only!")
            continue

        if guess in guessed_letters:
            print("❌ You already guessed that letter!")
            continue

        # Add guess to guessed letters
        guessed_letters.add(guess)

        # Check if guess is correct
        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word!")
        else:
            wrong_guesses += 1
            print(f"❌ Sorry, '{guess}' is not in the word!")

        print("-" * 40)

    # Game over - player lost
    print(display_hangman(wrong_guesses))
    print("💀 Game Over! You've been hanged!")
    print(f"The word was: {word.upper()}")


def main():
    """Main function to run the game"""
    while True:
        hangman_game()

        # Ask if player wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower().strip()
        if play_again != 'y' and play_again != 'yes':
            print("Thanks for playing Hangman! 👋")
            break
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
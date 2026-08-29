import random

def play_hangman():
    words = ['python', 'programming', 'internship', 'developer', 'software']
    
    print("====================================")
    print("      CODEALPHA HANGMAN GAME        ")
    print("====================================")
    print("Welcome to Hangman!")
    print("Try to guess the secret word one letter at a time.")
    print("You have a maximum of 6 incorrect guesses.")
    print("====================================\n")

    while True:
        secret_word = random.choice(words)
        guessed_letters = set()
        incorrect_guesses = 0
        max_attempts = 6
        
        while incorrect_guesses < max_attempts:
            # Display current progress
            current_progress = ""
            for letter in secret_word:
                if letter in guessed_letters:
                    current_progress += letter + " "
                else:
                    current_progress += "_ "
            
            print(f"Word: {current_progress.strip()}")
            print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
            print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
            
            # Check for win condition
            if "_" not in current_progress:
                print(f"\nCongratulations! You guessed the word '{secret_word}' correctly! You WIN!")
                break
                
            guess = input("\nEnter a letter: ").lower()
            
            # Input validation
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single alphabetic letter.")
                print("------------------------------------")
                continue
                
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try another letter.")
                print("------------------------------------")
                continue
                
            guessed_letters.add(guess)
            
            if guess in secret_word:
                print(f"Good guess! '{guess}' is in the word.")
            else:
                print(f"Wrong guess! '{guess}' is not in the word.")
                incorrect_guesses += 1
            print("------------------------------------")
            
        if incorrect_guesses == max_attempts:
            print(f"\nGame Over! You've run out of attempts.")
            print(f"The secret word was: '{secret_word}'")
            
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes' and play_again != 'y':
            print("Thank you for playing CodeAlpha Hangman! Goodbye.")
            break
        print("\nStarting a new game...\n")

if __name__ == "__main__":
    play_hangman()

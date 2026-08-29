# CodeAlpha Hangman Game

## Description
A simple, text-based Hangman game built in Python. This project is a submission for the CodeAlpha Python Internship Task 1. The game selects a random word from a predefined list, and the player must guess it one letter at a time before running out of attempts.

## Features
- **Random Word Selection:** The game randomly picks from a predefined list of 5 words.
- **Progress Tracking:** Clearly displays the correctly guessed letters and blanks for remaining letters.
- **Attempt Tracking:** The player has a maximum of 6 incorrect guesses.
- **Input Validation:** Prevents invalid inputs (like numbers, symbols, or multiple letters at once) and repeated guesses.
- **Replayability:** Asks the player if they want to play again after a round ends.
- **Clean Console Interface:** Neat and structured text output for a professional and beginner-friendly user experience.

## Technologies Used
- Python 3
- Standard Python libraries: `random`

## How the Game Works
1. The game selects a secret word from its list (`python`, `programming`, `internship`, `developer`, `software`).
2. The player is presented with blanks `_` representing each letter in the word.
3. The player inputs one letter per turn.
4. If the letter is in the word, it replaces the corresponding blank(s).
5. If the letter is not in the word, the player loses one of their 6 attempts.
6. The game ends when the player either guesses the entire word correctly (Win) or runs out of attempts (Loss).
7. The player can choose to play again or exit.

## How to Run the Project
1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the game.
4. Run the following command:
   ```bash
   python hangman.py
   ```

## Sample Gameplay Output
```text
====================================
      CODEALPHA HANGMAN GAME        
====================================
Welcome to Hangman!
Try to guess the secret word one letter at a time.
You have a maximum of 6 incorrect guesses.
====================================

Word: _ _ _ _ _ _ _
Incorrect guesses left: 6
Guessed letters: None

Enter a letter: a
Wrong guess! 'a' is not in the word.
------------------------------------
Word: _ _ _ _ _ _ _
Incorrect guesses left: 5
Guessed letters: a
...
```

## Concepts Learned
- Using the `random` module for unpredictable behavior.
- Utilizing `while` loops for game states and repetitive prompts.
- String manipulation and basic list/set operations.
- User input handling and validation.
- Control flow using `if-else` statements.

## About
- **Task:** Task 1 - Hangman Game
- **Internship:** CodeAlpha Python Internship

import random
import os

from hangman_art import stages, logo
from hangman_words import word_list

# Chose a word from the word list
print(logo)
chosen_word = random.choice(word_list)
# print(f"Chosen Word: {chosen_word}")
word_length = len(chosen_word)

# Create a list with as many blanks as number of characters in word list
display = []
for _ in range(word_length):
    display.append("_")

# Keep asking user for input until the user runs out of lives
lives_remaining = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Replace blank with character in display list if there is a match
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If the letter is not found in word reduce the lives remaining by 1
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives_remaining -= 1

    print(f"{' '.join(display)}")
    print(stages[lives_remaining])

    # The player looses when there are no lives left
    if lives_remaining == 0:
        print("You Lose!!")
        end_of_game = True

    # Game over if there are no more blanks in display list
    if "_" not in display:
        print("You Win!!")
        end_of_game = True

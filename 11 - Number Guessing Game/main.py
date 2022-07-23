import random
from art import logo


def calculate_attempts(difficulty_level):
    """Calculate the total attempts based on difficulty level selected by the user"""
    if difficulty_level == "easy":
        return 10
    else:
        return 5


def check_answer(guessed_number, generated_number, attempts_remaining):
    if guessed_number > generated_number:
        print("Too High.")
        attempts_remaining -= 1
    elif guessed_number < generated_number:
        print("Too Low.")
        attempts_remaining -= 1
    else:
        print(f"You got it! The answer was {generated_number}")
        attempts_remaining = -1

    if attempts_remaining == 0:
        print("Game over. You have no attempts remaining.")

    return attempts_remaining


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
selected_number = random.randint(0, 101)
print(selected_number)
diff_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

total_attempts = calculate_attempts(diff_level)

while total_attempts != 0 and total_attempts != -1:
    print(f"You have {total_attempts} attempts remaining to guess the number.")

    user_input = int(input("Make a guess: "))
    total_attempts = check_answer(user_input, selected_number, total_attempts)

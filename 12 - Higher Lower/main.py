from art import logo, vs
from game_data import data
import random


def generate_option():
    """Generates a random option and returns the question with follower as a dictionary"""
    option = {}
    option_data = random.choice(data)
    option_message = f"{option_data['name']}, a {option_data['description']}, from {option_data['country']} "
    option_follower = option_data['follower_count']
    option["message"] = option_message
    option["follower"] = option_follower
    return option


def generate_comparison_question(option_a, option_b):
    """Takes the 2 options as input, generates the comparison question, and provides option to the user to select.
    Returns the option selected by the user"""
    print(f"Compare A: {option_a['message']}")
    print(vs)
    print(f"Against B: {option_b['message']}")
    selected_option = input("Who has more followers? Type 'A' or 'B': ").lower()
    return selected_option


def highest_follower(option_a, option_b):
    """Return option with the highest follower count"""
    if int(option_a["follower"]) > int(option_b["follower"]):
        return "a"
    else:
        return "b"


def play_game():
    print(logo)
    result = 0
    continue_with_game = True
    option_2 = generate_option()

    while continue_with_game:
        option_1 = option_2
        option_2 = generate_option()

        while option_1 == option_2:
            option_2 = generate_option()

        user_selection = generate_comparison_question(option_1, option_2)

        if user_selection == highest_follower(option_1, option_2):
            result += 1
            print(f"You're right! Current score: {result}")
        else:
            continue_with_game = False
            print(f"Sorry, that's wrong. Final score: {result}")


play_game()

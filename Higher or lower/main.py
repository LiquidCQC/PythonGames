from tabnanny import check

from art import logo, vs
from game_data import data
import random



print(logo)
def rdm_list():
    data_length = len(data)
    choice_1 = random.randint(0, data_length - 1)  # Ensure choices are within valid range
    choice_2 = random.randint(0, data_length - 1)

    while choice_1 == choice_2:  # Avoid choosing the same celebrity twice
        choice_2 = random.randint(0, data_length - 1)

    print(f"Compare A: {data[choice_1]['name']},{data[choice_1]['description']},from {data[choice_1]['country']}")
    print(vs)
    print(f"Against B: {data[choice_2]['name']},{data[choice_2]['description']},from {data[choice_2]['country']}")

    a_followers = data[choice_1]["follower_count"]
    b_followers = data[choice_2]["follower_count"]

    return a_followers, b_followers

def check_answer(a_followers, b_followers):
    player_choice = input("Who has more followers? Type 'A' or 'B' : ").lower()
    return (player_choice == "a" and a_followers > b_followers) or (player_choice == "b" and a_followers < b_followers)

def game():
    game_is_on = True
    score_count = 0
    while game_is_on:
        a_followers, b_followers = rdm_list()  # Get follower counts directly in the loop
        correct_answer = check_answer(a_followers, b_followers)

        if correct_answer:
            score_count += 1
            print(logo)
            print(f"You're right! Current score: {score_count}")
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score_count}")
            game_is_on = False  # End the game after incorrect guess




game()


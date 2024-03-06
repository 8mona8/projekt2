"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""


import random

def generate_secret_code():
    return [random.randint(0, 9) for _ in range(4)]

def give_feedback(secret_code, guess):
    bulls = sum(1 for i, digit in enumerate(guess) if digit == secret_code[i])
    cows = sum(1 for digit in guess if digit in secret_code) - bulls
    return bulls, cows

def is_game_over(feedback):
    return feedback[0] == 4  # Game ends when all digits are correct and in the right position

# Example usage:
secret_code = generate_secret_code()

while True:
    guess = [int(x) for x in input("Enter your guess (4 digits): ")]
    feedback = give_feedback(secret_code, guess)
    print(f"Feedback: {feedback[0]} bull(s), {feedback[1]} cow(s)")

    if is_game_over(feedback):
        print("Congratulations! You've found the secret code.")
        break

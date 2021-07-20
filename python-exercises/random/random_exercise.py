"""
This is exercise for random
"""
import random as r
import string


def guessing_game():
    guess_count = 0
    result = r.randint(1, 9)
    while 1:
        print("Please enter your answer or exit to exit the game")
        ans = input()
        guess_count += 1
        if ans.isdigit():
            if int(ans) == result:
                print(f"Congratulation you win the game!, guess count: {guess_count}")
                break
            elif int(ans) < result:
                print("Too low")
            else:
                print("Too high")
        elif ans == "exit":
            print("Exit the game!")
            break
        else:
            print("Unknown command")


def password_generator():
    # Get all characters from string library
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    # Append all characters into data
    data = lower + upper + num + symbols

    # Take random from 8 to 12 characters from data
    raw_pass = r.sample(data, r.randint(8, 12))

    # Print out the generated password
    print("".join(raw_pass))

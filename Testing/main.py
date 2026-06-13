import random

def check_guess(guess, number):
    if not 1 <= guess <= 100:
        return "invalid"

    if guess == number:
        return "correct"

    if guess > number:
        return "high"

    return "low"

number = random.randint(1, 100)
if __name__ == '__main__':
    while True:
        guess = int(input("Enter your guess: "))

        result = check_guess(guess, number)

        if result == "correct":
            print("Hurray! You guessed it correctly.")
            break

        elif result == "high":
            print("Your guess is too high.")

        else:
            print("Your guess is too low.")
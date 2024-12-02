import random

def level():
    lev = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if lev == "easy":
        return 10
    elif lev == "hard":
        return 5
    else:
        print("Invalid difficulty. Defaulting to 'easy'.")
        return 10

def main():
    number_to_guess = random.randint(1, 100)  # assuming the range is 1 to 100
    print("Welcome to the Number Guessing Game!")
    lives = level()  # or however many lives you want to give the player

    while lives > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Congratulations! You've guessed the number.")
                break
        except ValueError:
            print("Please enter a valid number.")
            continue

        lives -= 1
        print(f"Lives left: {lives}")

        if lives == 0:
            print("Game Over! You've run out of lives.")
            break


if __name__ == "__main__":
    main()

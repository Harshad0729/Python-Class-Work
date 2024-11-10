import random

# Generate a random number between 0 and 20
magic_number = random.randint(0, 20)

# Prompt user to start guessing
print("Guess the magic number between 0 and 20:")

while True:
    # Get user's guess and convert it to an integer
    guess = int(input("Enter your guess: "))

    # Check if the guess is correct
    if guess == magic_number:
        print("Congratulations! You guessed the magic number!")
        break
    else:
        print("Wrong guess! Try again.")

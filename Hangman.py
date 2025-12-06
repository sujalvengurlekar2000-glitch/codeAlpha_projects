import random

words = ["python", "hangman", "computer", "program", "random","Shubham","sujal"]

# Pick a random word
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {max_incorrect} incorrect guesses allowed.\n")

# Game loop
while incorrect_guesses < max_incorrect:
    
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")

    # Player input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("Good guess!\n")
    else:
        print("Wrong guess!\n")
        incorrect_guesses += 1

    # Check if player won
    if all(letter in guessed_letters for letter in secret_word):
        print(f"Congratulations! You guessed the word: {secret_word}")
        break

# Player loses
if incorrect_guesses == max_incorrect:
    print(f"Game Over! The word was: {secret_word}")
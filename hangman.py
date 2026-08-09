import random

# 5 predefined words
words = ["apple", "tiger", "school", "python", "computer"]

# Randomly select a word
word = random.choice(words)

# Hide the word
guessed_word = ["_"] * len(word)

# Game variables
incorrect_guesses = 0
max_guesses = 6
guessed_letters = []

print("================================")
print("          HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

while incorrect_guesses < max_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

    guess = input("Guess a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    # Wrong guess
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Check result
if "_" not in guessed_word:
    print("\n================================")
    print("Congratulations! You won!")
    print("The word was:", word)
    print("================================")
else:
    print("\n================================")
    print("Game Over!")
    print("The word was:", word)
    print("================================")
import random

print("================================")
print("   WELCOME TO HANGMAN GAME!")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 chances to guess wrong.\n")

words = ["apple", "tiger", "house", "chair", "plant"]

word = random.choice(words)

guessed = ["_"] * len(word)

wrong = 0

while wrong < 6:

    print("Word:", " ".join(guessed))

    letter = input("Guess a letter: ")

    if letter in word:

        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("Correct!")

    else:
        wrong = wrong + 1
        print("Wrong!")

    if "_" not in guessed:
        print("You won!")
        break

if wrong == 6:
    print("You lost!")
    print("The word was:", word)
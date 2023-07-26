import random
from hangman_art import stages, logo
from hangman_words import words

print(logo)
print(
    "Rules:\n1.Computer will choose a Random Animal Name,You have to guess the animal name by letters"
    "\n2.You will lose lives if you misguess the letters 6 times"
    "\n3.Every time you misguess the letters you make make the hangman near to death by hanging")

chosen_word_raw = random.choice(words)
chosen_word = chosen_word_raw.lower()
word_length = len(chosen_word)
lives = 6
end_of_game = False
display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    user_guess = input("Guess the letter:").lower()

    if user_guess in display:
        print(f"You've already guessed {user_guess}")

    for indexposition in range(word_length):
        check = chosen_word[indexposition]
        if check == user_guess:
            display[indexposition] = user_guess

    if user_guess not in chosen_word:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("You lose the game")
            end_of_game = True

    print(" ".join(display))

    if "_" not in display:
        print("You win")
        end_of_game = True


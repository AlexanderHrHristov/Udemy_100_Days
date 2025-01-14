import random
from Hangman_Words import word_list
from Hangman_Art import stages

lives = 6

choosen_word = random.choice(word_list)
print(choosen_word)

placeholder = ""
worf_lenght = len(choosen_word)
for position in range(worf_lenght):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in choosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not the word. You lose a life.")
        print(stages[lives])

        if lives == 0:
            game_over = True

            print(f"**********It Was {choosen_word.upper()} ! You Lose!**********")

    if "_" not in display:
        game_over = True
        print("**********YOU WIN!***********")

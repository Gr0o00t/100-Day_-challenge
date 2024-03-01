from Word_list import Words
import random
import os

Choosen_word=random.choice(Words)
end_game = False
word_length = len(Choosen_word)

lives = 6
#print(f'psst, The Solution is {Choosen_word}')

display = []
for _ in range (word_length):
    display += "_"

while not end_game:
    guess = input("Guess a letter").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = Choosen_word[position]
        if letter ==guess:
            display[position]= letter

    if guess not in Choosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives-=1

        if lives == 0:
            end_game=True
            print("You Lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You Win. ")

    from Hangman_logo import stages
    print(stages[lives])

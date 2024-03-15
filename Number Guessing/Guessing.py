EASY_LIVES=10
HARD_LIVES=5

import random
choosen_number=random.randint(1,100)
    #print(choosen_number)

is_game_over = False
game_level= input("Choose a Difficulty: Type 'EASY' or 'HARD'").upper()
if game_level=='EASY':
    lives=EASY_LIVES
else:
    lives=HARD_LIVES
while not is_game_over:
    print(f"You have {lives}, to guess the number")
    if lives==0:
        print(f"You Lose, Computer's number: {choosen_number}")
        is_game_over = True
    else:
        choosen=eval(input("Enter your choice"))
        if choosen > choosen_number:
            print("Too High")
            lives-=1
        elif choosen < choosen_number:
            print("Too Low")
            lives-=1
        else :
            print("YOU WIN")
            is_game_over =True

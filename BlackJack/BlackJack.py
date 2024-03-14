import Pick_random_card

user_cards=[]
computers_card=[]
is_game_over=False

for _ in range(2):
    user_cards.append(Pick_random_card.Pick_random())
    computers_card.append(Pick_random_card.Pick_random())
while not is_game_over:

    sum_user=Pick_random_card.calcualte_score(user_cards)
    sum_computer=Pick_random_card.calcualte_score(computers_card)
    print(f"Your cards {user_cards} and sum of those is {sum_user}")
    print(f"Computer first card {computers_card[0]}")
    if sum_user==0 or sum_computer==0 or sum_user>21:
        is_game_over=True
    else:
        user_should_deal=input("Tyoe 'y' to get the another card, type 'n' to pass: ").upper()
        if user_should_deal == 'Y':
            user_cards.append(Pick_random_card.Pick_random())
        else:
            is_game_over=True

while sum_computer !=0 and sum_computer < 17:
    computers_card.append(Pick_random_card.Pick_random())
    sum_computer = Pick_random_card.calcualte_score(computers_card)
print(f"Your Final Hand: {user_cards}, final score: {sum_user}")
print(f"Computer's Final Hand: {computers_card}, final score: {sum_computer}")
print(Pick_random_card.compare(sum_user,sum_computer))
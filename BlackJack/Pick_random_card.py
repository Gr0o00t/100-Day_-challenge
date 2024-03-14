import random
def Pick_random():
    """Return A random Card from Deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card =random.choice(cards)
    return card

def calcualte_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score,computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score ==0:
        return "Lose, oppenent has blackjack"
    elif user_score ==0:
        return "WIN, with a Blackjack"
    elif user_score > 21:
        return "You went Over. You Lose"
    elif computer_score > 21:
        return "Opponent went over, You Win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"
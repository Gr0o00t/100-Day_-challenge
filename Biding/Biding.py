Bids = {}
biding_finished= False

def find_highest_bid(bid_record):
    highest_bid=0
    winner=""

    for bidders in bid_record:
        bid_amount=bid_record[bidders]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidders
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print("Welcome to the secret autcion program")

while not biding_finished:
    name=input("Enter the name of bidder")
    amount= int(input("Enter the bid Amount"))
    Bids[name]=amount
    should_continue= input("Please enter YES : For more bidders and enter NO for over").upper()

    if should_continue=="NO":
        biding_finished=True
        find_highest_bid(Bids)

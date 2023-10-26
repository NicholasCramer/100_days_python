from art import logo

print(logo)

def clear():  # Prints 50 blank lines
    print("\n" * 50)


def find_highest_bidder(bidding_log):
    highest_bid = 0
    winner = ""
    for bidder in bidding_log:
        bid_amount = bidding_log[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of ${highest_bid}.")


continue_bidding = True
while continue_bidding:
    bids = {}
    bidder_name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[bidder_name] = bid

    print("Any more bidders?")
    response = input().lower()
    if response == "yes":
        clear()
    else:
        continue_bidding = False
        find_highest_bidder(bids)




def find_highest_bid(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"winner is {winner} with a bid of ${highest_bid}.")
# name = input("what's your name?: ")
# price = int(input("what's you bid?: $"))
#
bids = {}
#
# bids[name] = price

continue_bidding = True
while continue_bidding:
    name = input("what's your name?: ")
    price = int(input("what's you bid?: $"))
    bids[name] = price
    should_continue = input("are there any other bidder? Type 'yes' or 'no'.\n").lower()
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bid(bids)
    elif should_continue == 'yes':
        print("\n"*20)


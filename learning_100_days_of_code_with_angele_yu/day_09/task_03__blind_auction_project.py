import art
print(art.logo)

# 4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        # Also we can use max() function that can figure out what is
        # the maximum value of all the values in a dictionary 👇
        # winner = max(bidding_dictionary, key=bidding_dictionary.get) ✅
        # highest_bid = bidding_dictionary[winner]                     ✅

    print(f"The winner is {winner} with a bid of ${highest_bid}")



continue_bidding = True
bids = {}
while continue_bidding:
    # 1: Ask the user for input
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    # 2: Save data into dictionary {name: price}
    bids[name] = price

    # 3: Whether if new bids need to be added
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue == "yes":
       print("\n" * 100)    # Clear the output ==> by printing "\n" many times so that the screen scrolls down ✅
    elif should_continue == "no":
        continue_bidding = False
        print("\n" * 100)
        find_highest_bidder(bids)       # Calling function() ✅

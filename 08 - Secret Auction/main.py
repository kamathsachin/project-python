from art import logo

print(logo)
print("Welcome to the secret auction program.")

continue_bidding = True
bidding_data = {}

while continue_bidding:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bidding_data[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")

    if more_bidders == "no":
        bidder_name = max(bidding_data, key=lambda key: bidding_data[key])
        bidder_amount = bidding_data[bidder_name]

        print(f"The winner is {bidder_name} with a bid of ${bidder_amount}")

        continue_bidding = False

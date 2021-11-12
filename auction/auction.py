
from auction_art import logo
import os

def auction():

    auction_over = False
    auction_list = []
    

    while auction_over == False:

        auction_bids = {}

        print(logo)
        bidder_name = input("What is the bidder's name? ")
        bidder_amount = input("What is their bid? ")
     
        auction_bids["bidder"] = bidder_name
        auction_bids["bid amount"] = bidder_amount

        auction_list.append(auction_bids)

        print(auction_list)

        bidding_over = input("Continue auction? yes/no ").lower()

        if bidding_over == "no":
            auction_over = True
        
        os.system('cls')
    
    hi_bid = 0

    for num in (0, len(auction_list)-1):

        winner = ''
        cur_dict = auction_list[num]
        if int(cur_dict["bid amount"]) > hi_bid:
            winner = cur_dict["bidder"]
            hi_bid = cur_dict["bid amount"]

    print(f"The winning bid is {hi_bid} placed by {winner}")

        



auction()
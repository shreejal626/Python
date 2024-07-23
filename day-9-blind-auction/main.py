from replit import clear
import replit
#HINT: You can call clear() to clear the output in the console.

import art

print(art.logo)

bids = {}
repeat = True

def find_highest_bidder(bidding_record):
 highest_bid = 0
 winner = ""
 for bidder in bidding_record:
  bid_amount = bidding_record[bidder]
  if bid_amount > highest_bid:
   highest_bid = bid_amount
   winner = bidder
 print(f"{winner} is the winner.")
 
while repeat:
 name = input("Enter your name: ")
 price = int(input("Enter your bid amount: $"))
 bids[name] = price
 
 result = input("continue? ")
 if result == "no":
  repeat = False
  clear()
  find_highest_bidder(bids)
 elif result == "yes":
  clear()
 
  
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
more_bidders=True
bidding_data={}
while more_bidders:
    name=input("what is your name ?\n")
    bid_amount=int(input("how much you wannna bid ?\n"))
    other_bidders=input("are there any other bidders types yes or no ? \n").lower()
    print(more_bidders)
    
    bidding_data[name]=bid_amount
    


    if(other_bidders=="no"):
         more_bidders=False
       # print(more_bidders)
    print(bidding_data)
winner_name=''
highest_bid=0
for bid in bidding_data:
    
    bid_amounts=bidding_data[bid]
    print(bid_amounts)
    if(bid_amounts>highest_bid):
        highest_bid=bid_amounts
        winner_name=bid
print(f"winner is {winner_name} bidding amount was {highest_bid}")



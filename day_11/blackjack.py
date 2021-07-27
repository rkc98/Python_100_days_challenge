############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards=[]

user_cards.append(random.choice(cards))
user_cards.append(random.choice(cards))

computer_cards=[]
computer_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))

print(user_cards)
print(sum(computer_cards))
print(f"you cards are {user_cards} total points are {sum(user_cards)}")
print(f"computer first card is {computer_cards[0]}")
continue_game=True
while continue_game:
    user_input=input("press y to get a new card or n to pass").lower()
    if user_input=='y' and sum(user_cards)<21:
        user_cards.append(random.choice(cards))
        print(f"you cards are {user_cards} total points are {sum(user_cards)}")
    elif user_input=='n' and sum(computer_cards)<21:
        while sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))
        print(f"computer cards are {computer_cards} total points are {sum(computer_cards)}")
        continue_game=False
    if sum(user_cards) > 21:
       continue_game=False
print(f"you final score are {user_cards} total points are {sum(user_cards)}")
print(f"computer's final  are {computer_cards} total points are {sum(computer_cards)}")
print(sum(user_cards))
print(sum(computer_cards))
if sum(user_cards)>sum(computer_cards) and sum(user_cards)< 22:
    print("you won")
else:
    print("computer won")





        










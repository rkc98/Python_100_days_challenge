#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
numbers=[]
for i in range(1,101):
    numbers.append(i)
print(numbers)

random_number=random.choice(numbers)
attempts=10
user_input=input("chooose : difficulty 'easy' or 'hard'\n").lower()
print(random_number)
if(user_input=='hard'):
    attempts=5
while(attempts>0):
    print(f"you have got {attempts} remaining to guess the number")
    user_number_choice=int(input("please choose a number\n"))
    if(user_number_choice<random_number):
        print("too low")
    elif user_number_choice>random_number:
        print("too high")
    else:
        print("you have guessed the number")
        break
    attempts-=1
print("you have run out of guesses so you loose")



import random
from typing import List
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

map=[rock,paper,scissors]

print(f"{rock}\n{paper}\n{scissors}")

computer=random.randint(0,2)
user=int(input("write 0 for rock 1 for paper 2 for scissors \n"))
print(map[user])
print(map[computer])
# if(user==computer):
#     print("you won the match")
# else:
#     print("you lost")0

if(user==0 and computer==2):
    print("you won")
elif(user==1 and computer==0):
    print("you won")
elif(user==2 and computer==1):
    print("you won")
elif(user==computer):
    print("draw")
else:
    print("you lost")




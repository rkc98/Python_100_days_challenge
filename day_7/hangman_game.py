import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["samsung", "google", "apple"]
chosen_word = random.choice(word_list)

print(chosen_word)
display = []
for i in range(0, len(chosen_word)):
    display.append('_')
print(display)
num=0
stages_lenght=len(stages)-1
while num<len(stages):
    guess = input("guess the word\n").lower()
    for i in range(len(chosen_word)):
       if chosen_word[i] == guess:
           display[i] = guess
    if guess not in chosen_word:
        print(stages[stages_lenght])
       
    stages_lenght-=1
    print(display)
    num+=1
if '_' not in display:
    print("you wont the game")
else:
    print("you lost")
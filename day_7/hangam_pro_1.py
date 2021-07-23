import random


word_list = ["samsung", "google", "apple"]
chosen_word = random.choice(word_list)

print(chosen_word)
display = []
for i in range(0, len(chosen_word)):
    display.append('_')
print(display)
while '_' in display:
    guess = input("guess the word\n").lower()
    for i in range(len(chosen_word)):
       if chosen_word[i] == guess:
        display[i] = guess
    print(display)
if '_' not in display:
    print("you wont the game")
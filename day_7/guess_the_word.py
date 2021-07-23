import random
words__list=["cow","bull","camel"]


random_word=random.choice(words__list)



user_choice=input("guess a word which could be there ?\n").lower()
# if user_choice==random_word:
#     print("you have guessed it right")
# else:
#     print("you are wrong")

for letter in random_word:
    if user_choice==letter:
        print("you have guessed it right")
    else:
        print("Wrong")






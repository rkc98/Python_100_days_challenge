import art
import game_data
import  random
# print(art.logo)
# print(len(game_data.data))
random_a=random.choice(game_data.data)
game_data.data.remove(random_a)
# print(len(game_data.data))

random_b=random.choice(game_data.data)
# print(random_a,random_b)
# print(removed_item)
# print(len(game_data.data))
print(art.logo)
# print(f"compare A : {random_a['name']}, a {random_a['description']} from {random_a['country']} ")
# print(art.vs)
# print(f"compare B : {random_b['name']}, a {random_b['description']} from {random_b['country']} ")
game_start=True
count=0
while game_start:
    print(f"compare A : {random_a['name']}, a {random_a['description']} from {random_a['country']} ")
    print(art.vs)
    print(f"compare B : {random_b['name']}, a {random_b['description']} from {random_b['country']} ")
    user_choice=input("who has more follower 'A' or 'B': ").lower()
    if user_choice=="a":
        if random_a['follower_count'] > random_b['follower_count']:
            count+=1
            random_a=random.choice(game_data.data)
            random_b=random.choice(game_data.data)
            print(f"you are right current score is {count}")
        else:
            game_start=False
    elif user_choice=="b":
        if random_b['follower_count'] > random_a['follower_count']:
            count+=1
            random_b=random.choice(game_data.data)
            random_a=random.choice(game_data.data)
            print(f"you are right current score is {count}")
        else:
            game_start=False
print(f"sorry thats wrong you final score is {count}")
        





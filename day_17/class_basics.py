class User:
    def __init__(self,user_id,username):
        self.user_id=user_id
        self.username=username
        self.follower=0
        self.following=0
    def follows(self,user):
        user.follower+=1
        self.following+=1

user1=User(11,"krsna")
user2=User(1,"chaitanya")
user1.follows(user2)

print(user1.follower,user1.following)
print(user2.follower,user2.following)

    
        
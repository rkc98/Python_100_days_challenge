print('''
_||__ ____ ____ ____
  (o)___)}___}}___}}___}
  'U'0 0  0 0  0 0  0 0  :dg:
''')
print('Welcome to the treasure island')
print('your mission is to find treasure island')

direction=input("where do you wanna go ? \n")
if(direction=="right"):
    next_step=input("what to swim or fly")
    if(next_step=="fly"):
        select=input("what color door you wanna enter")
    
        if(select=="yellow"):
            print("you won the game")
        if(select=="blue"):
            print("wrong door")
        else:
            print('you have entered a  wrong door')
    else:
        print('whale ate you wrong door')       
else:
    print("game over try again")
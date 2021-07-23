scores = input("enter the highest score of all students").split()

for i in range(0, len(scores)):
    scores[i] = int(scores[i])  #converting string to int elements of the array
print(scores)

highest = 0
for i in range(0, len(scores)):
    if(highest < scores[i]):
        highest = scores[i]
print(highest)
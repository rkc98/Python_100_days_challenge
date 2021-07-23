heights=(input("input a list of students heights").split())

print(heights)
length=len(heights)
sum=0
for i in heights:
    sum=sum+int(i)
print(sum)
average=sum/length
print(average)
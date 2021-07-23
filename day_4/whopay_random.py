import random
getnames=input("give everybody name seperated by , commas")

split_names=getnames.split(', ')
print(split_names)
num_of_names=len(split_names)
random_num=random.randint(0,num_of_names-1)
name_selected=split_names[random_num]

print(f"{name_selected} is gonna pay the bill")

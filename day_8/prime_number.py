
check_number=int(input("check this number:\n"))

def primechecker(check_number):
    temp=0
    for i in range(2,check_number):
         if check_number%i==0:
             temp+=1
    if temp > 0:
        print("not prime ")
    else :
        print("prime number")
primechecker(check_number)





def calculate(a,b,sign):
    if sign == "+":
        return a+b
    elif sign == "-":
        return a-b
    elif sign == "*":
        return a*b
    elif sign == "/":
        return a/b
    else:
        return "please check your inputs"
check=True
while check:
    num_1 = float(input("enter you first number: "))
    operation = input("what you wanna perform amongst(+,-,*,/): ")
    num_2 = float(input("enter you second number: "))
    result=calculate(a=num_1,b=num_2,sign=operation)
    print(result)
    if input("click y to continue calculating: ").lower()=='y':
        check=True
    else:
        check=False

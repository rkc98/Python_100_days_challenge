print("Welcome to the tip calculator.")

bill_amount=float(input("what was your total bill? \n $"))
num_of_people=int(input("between how many peoplr you would like to split ?\n"))
percentage=int(input("what percentage tip would you like to give ?\n"))
total_amount=int(bill_amount*(1+percentage/100))
each_person_pay=total_amount/num_of_people
final_amount=round(each_person_pay,2)
print(f"each one has to pay {final_amount}")






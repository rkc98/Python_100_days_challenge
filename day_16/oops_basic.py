# from turtle import Turtle,Screen

# timmy=Turtle()   #object creation in python
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# print(timmy)
# timmy.forward(100)

from prettytable import PrettyTable

table=PrettyTable()
table.add_column("pokemon",["Pikachu","richu","charmender"])
table.add_column("type",["electric","basic","fire"])
table.align="l"
print(table)

# from turtle import Turtle, Screen
#
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOrchid")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()



table.add_column("Pokemon Name",["Chespin","Quilladin","Fennekin"])
table.add_column("Type",["Grass","Grass","Fire"])
table.align = "l"
print(table)
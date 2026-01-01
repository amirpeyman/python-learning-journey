# Object-Oriented Programming (OOP) 👇

# Using a library of code (here the Turtle library) that someone else created 👇

from turtle import Turtle, Screen   # import Turtle Class from turtle module ✅

timmy = Turtle()                    # Construct or create a new object called 'timmy' ✅
print(timmy)
timmy.shape("turtle")               # Object's method syntax ==> object.method() ==> timmy.shape("turtle") ✅
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)         # Object's attribute syntax ==> object.attribute ==> my_screen.canvheight ✅

my_screen.exitonclick()             # Object's method syntax ==> object.method() ==> my_screen.exitonclick() ✅

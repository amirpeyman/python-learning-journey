# Python Tuples ==> Ordered & Immutable Data Type (Carved in stone) 👇
my_tuple = (1, 3, 8)
print(my_tuple[2])
# my_tuple[1] = 5           # ❌ TypeError

person = ("Ali", 25, "Tehran")
print(person[0])
# person[0] = "Amir"        # ❌ TypeError


# Use Python Tuples to Generate Random RGB Colors 👇
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)            # To use RGB format in Turtle Graphics, we need to set the module's color mode to 255 ❗

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()

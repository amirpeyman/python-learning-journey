# Python Event Listeners 👇

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()         # Instruct the target object to start listening ✅

# When using methods or functions we didn't define ourselves, it's better to use keyword arguments when calling them 👇❗
screen.onkey(key="space", fun=move_forwards)    # When passing a function as an argument,
                                                # do not add parentheses at the end ⚠️
screen.exitonclick()



# Python Higher-Order Functions 👇

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Here, the calculator function is a higher-order function because it can work with another function as an input or output 👇✅
def calculator(n1, n2, func):
    return func(n1, n2)

result = calculator(2, 3, add)
print(result)

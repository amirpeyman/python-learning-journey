from turtle import Turtle, Screen

# Object Instances ==> Each object generated from a class is called an 'instance' 👇
timmy = Turtle()
tommy = Turtle()


# Object State ==> The collection of data stored inside an object instance is called its 'state' 👇

timmy.color("green")    # the state of Timmy's color attribute is green
timmy.forward(100)      # the state of Timmy's forward attribute is 100

tommy.color("purple")   # the state of Tommy's color attribute is purple
tommy.left(50)          # the state of Tommy's left attribute is 50



screen = Screen()
screen.exitonclick()

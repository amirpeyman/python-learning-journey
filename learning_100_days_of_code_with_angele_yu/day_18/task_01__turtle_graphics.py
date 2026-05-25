# Understanding Turtle Graphics 👇

from turtle import Turtle, Screen

# A programmer should be able to read and use module documentation effectively,
# and know how to search for solutions (especially using Google and Stack Overflow). ⚠️
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")       # https://www.tcl-lang.org/man/tcl8.4/TkCmd/colors.htm ✅
                                    # Tkinter is the standard GUI (Graphical User Interface) library for Python
                                    # Tkinter is the standard Python interface to the Tk GUI toolkit
                                    # Tk is the toolkit that the Turtle module uses to create the GUI

timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)


screen = Screen()
screen.exitonclick()

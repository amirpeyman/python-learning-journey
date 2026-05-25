# Importing Modules, Installing Packages, and Working with Aliases 👇

# Types of Import Modules 👇
# 1️⃣ Basic Import ==> Suitable if used only once or twice ✅
import turtle
tim = turtle.Turtle()


# 2️⃣ from...import... ==< Suitable if used three or more times ✅
from turtle import Turtle
timmy = Turtle()


# 3️⃣ Everything Import ==> Code works, but it's really confusing. it's unsuitable ❌
from random import *
choice([1, 2, 3])


# 4️⃣ Aliasing Modules Import ==> Suitable when used multiple times or for long module names ✅👌
import turtle as t
timmy_the_turtle = t.Turtle()




# Installing Modules 👇
import heroes           # Sometimes, if a module is not included in the Python standard library,
                        # you may need to install it. ❗
print(heroes.gen())


# When we install a new package or module (for example, from PyPI),
# it is installed in the "local virtual environment" of the current project.
# You can find it inside the project's .venv directory.

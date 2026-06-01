# Class Inheritance 👇

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")


class Fish(Animal):                         # 'Fish' is SubClass, 'Animal' is SuperClass ✅
    def __init__(self):
        super().__init__()                  # Calls the parent class constructor ✅

    def breathe(self):
        super().breathe()                   # Has the same functionality as the superclass ✅
        print("doing this underwater.")     # Do something extra ✅

    def swim(self):
        print("Moving in water.")



nemo = Fish()

nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

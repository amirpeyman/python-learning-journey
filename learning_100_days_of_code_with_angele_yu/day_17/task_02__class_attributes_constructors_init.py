# Working with Attributes, Class Constructors and the __init__() Function 👇

class User:
    pass

# Associate attributes with objects 👇
user_1 = User()
user_1.id = "001"
user_1.username = "peyman"
print(user_1.id)
print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "amir"
print(user_2.id)
print(user_2.username)


# Constructors ==> Initialize objects with __init__ function 👇✅
class User:
    def __init__(self):     # In fact, 'self' refers to the 'user_1' object ✅
        print("new user being created...")

user_3 = User()     # init function is going to be called every time that create a new object from class ❗


# Set up object attributes 👇
class Car:
    def __init__(self, seats):
        self.seats = seats

my_car = Car(5)
print(my_car.seats)


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

user_4 = User("004", "apn") # The ID '004' is passed to the 'user_id' parameter in the constructor ❗
print(user_4.id)
print(user_4.username)
print(user_4.followers)

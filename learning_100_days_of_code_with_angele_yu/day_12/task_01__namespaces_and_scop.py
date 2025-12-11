# Namespaces ==> Local Scope vs Global scope 👇

enemies = 1         # Variables or functions declared at the top level (unindented) of a code file have 'global scope'
                    # It is accessible anywhere in the code file ✅



def increase_enemies():
    enemies = 2     # Variables or functions declared inside functions have 'local scope' (also called function scope)
                    # They are only seen by other code within the same block of code ✅
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope 👇
def drink_potion():
    potion_strength = 2         # This variable has 'local scope' ✅
    print(potion_strength)

drink_potion()
print(potion_strength)          # It gives an error because the variable has local scope ❌


# Global Scope 👇
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)        # This variable has 'global scope' ✅

drink_potion()

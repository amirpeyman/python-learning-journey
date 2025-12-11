# Global Vars / Modifying Global Scope 👇

enemies = 1

def increase_enemies():
    global enemies      # Use the keyword 'global' to force the code to modify something global ✅
    enemies += 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")






# ************************************************************************************************

enemies = 1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1    # The logical and better way to change the value of a global variable ✅


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

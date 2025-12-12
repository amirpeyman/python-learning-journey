import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2                         # this highlighted line is called 'Breakpoint'.
                                                    # This line will be where the program pauses during debug run.
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)                         # After using the debugger, we find that the bug is in this line ❌
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

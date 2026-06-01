# Slicing in Python ==> means taking a portion of a sequence, such as a list, tuple, or string ✅ 👇

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])      # 'c', 'd', 'e'             # the stop value itself is not included in the output ❗
print(piano_keys[2:])       # 'c', 'd', 'e', 'f', 'g'
print(piano_keys[:3])       # 'a', 'b', 'c'
print(piano_keys[1:5:2])    # 'b', 'd'
print(piano_keys[1::2])     # 'b', 'd', 'f'
print(piano_keys[::2])      # 'a', 'c', 'e', 'g'
print(piano_keys[::-1])     # 'g', 'f', 'e', 'd', 'c', 'b', 'a'     # for reverse list ✅


piano_tuple = ("do", "re", "me", "fa", "so", "la", "ti")    # 'me', 'fa', 'so'

print(piano_tuple[2:5])


text = "Python"

print(text[0:3])   # Pyt
print(text[2:])    # thon
print(text[:4])    # Pyth
print(text[::2])   # Pto
print(text[::-1])  # nohtyP

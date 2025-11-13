# Challenge 1
# # Printing each character of the word "Factory" incrementally repeated on each line.#
# F
# aa
# ccc
# tttt
# ooooo
# rrrrrr
# yyyyyyy

# Java
counter = 1
for char in "Factory":
  print(char * counter)
  counter += 1

print("-" * 31)

# Python style
for i in range(len("Factory")):
  print("Factory"[i] * (i + 1))

# Challenge 2
# # Printing each character of the word "Factory" incrementally repeated on each line.#
# F******
# aa*****
# ccc****
# tttt***
# ooooo**
# rrrrrr*
# yyyyyyy

# Python style
# 1st method
for i in range(len("Factory")):
  print("Factory"[i] * (i + 1) + "*" * (len("Factory") - (i + 1)))
# 2nd method
for i in range(len("Factory")):
  print("Factory"[i] * (i + 1), end="*" * (len("Factory") - (i + 1)))
  print()

print("*" * 31)

for num in range(17):
  print(num, end=" ")
print()
print(num) # 16
# Δεν υπάρχει block scope στη Python για αυτό θα τυπώσει 16.
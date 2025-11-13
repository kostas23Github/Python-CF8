message = "Coding Factory"

print(message[0]) # C
print(message[1]) # o
print(message[2]) # d
print(message[3]) # i
print(message[4]) # n
print(message[5]) # g

# spoiler
print(message[0:4]) # from 0 to 4

# String immutable
# message[0] = "K"

# iterate str with simple for-loop
for char in message:
  print(char, end="")  # overload "\n", to "", *by default after each print a new line char is added*
print()

# range
a = range(100_000_001)
print()

for i in a:
  if i > 9:
    break
  print(i, end=" ")
print()

# length of string
str_length = len(message)
print(f"Length of {message} is {str_length}")

for i in range(len(message)):
  print(message[i], end="\t") # for i in 14 add a tab


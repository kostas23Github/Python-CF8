# Define a tuple of students
students = "Alice", "Bob", "Charlie"

print("Initial tuple:", students)
# Check the type of the tuple
print(type(students))

# Iterate over the tuple with index and value
for index, student in enumerate(students):
    print(f"{index} : {student}")

# Enhanced for-loop to iterate over values only
for student in students:
    print(student)

# Unpacking tuple elements into variables
first_st, second_st, third_st = students[0], students[1], students[2]
first_st2, second_st2, third_st2 = students

print(f"first student: {first_st}")
print(f"first student: {first_st2}")
print(f"first student: {second_st}")
print(f"first student: {second_st2}")
print(f"first student: {third_st}")
print(f"first student: {third_st2}")

# Modifying tuple elements by converting to a list and back
students = list(students)  # Convert tuple to a list
students[0] = "Panagiotis"  # Modify the first element
students = tuple(students)  # Convert the list back to a tuple

# Print the modified tuple and its type
print(students)
print(type(students))
sum = {
  "key1" : "value1",
  "key2" : 10,
  3 : [1, 2, 3],
  4 : {1: "one", 2: "two"}
}
print(sum)

for key, value in sum.items():
  print(key, ":", value)

# TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
# sum = {
#   {1, 2, 3} : "Hello CF8",
#   "key1" : "value1",
#   "key2" : 10,
#   3 : [1, 2, 3],
#   4 : {1: "one", 2: "two"}
# }

# Define a dictionary with diverse key-value pairs
sym = {
    frozenset({1, 2, 3}): "Hello",  # Immutable frozenset as a key
    "key1": "value1",  # String key with string value
    "key2": 10,  # String key with integer value
    3: [1, 2, 3],  # Integer key with list value
    4: {1: "one", 2: "two"}  # Integer key with nested dictionary as value
}

# Print the entire dictionary
print(sym)
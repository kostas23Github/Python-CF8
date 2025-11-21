# Dictionary CRUD functions

# dictionaries dont have order BUT for print()
# Initial dictionary of products
products = {1: "apples", 2: "bananas", 10: "honey", 3: "melons"}
print("Initial products:", products)

# products2 = {1:"apples", [2, 3, 4]: 30}  # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
products3 = {1:"apples", "ages": [2, 3, 4]}  # valid

# Create: Insert a new item
products[3] = "oranges"
print("\nAfter inserting key 3 with value 'oranges':", products)

# Read: Access elements by key
product_10 = products.get(10, "Not Found")
print("\nProduct with key 10:", product_10)

# .get(item, default_value)
product_100 = products.get(100, "Product key not found")
print(product_10)

# Update: Change the value of an existing item
products[2] = "milk"
print("\nAfter updating key 2 to 'milk':", products)

# Delete: Remove an item by key using del
del products[1]
print("\nAfter deleting key 1:", products)

# Delete: Remove an item by key using pop() and handle potential KeyError
# .pop(value, default_value)
removed_product = products.pop(3, "Not Found")
print("\nAfter popping key 3:", products)
print("Popped product:", removed_product)

# Delete: Remove the last inserted item using popitem()
key, value = products.popitem()
print("\nAfter popping the last item inserted:", products)
print(f"Popped item - Key: {key}, Value: {value}")

# Check for key existence
key_to_check = 2
if key_to_check in products:
    print(f"\nKey {key_to_check} exists in products.")
else:
    print(f"\nKey {key_to_check} does not exist in products.")

# Iterating through keys
print("\nIterating through keys:")
for key in products.keys():
    print(f"Key: {key}, Value: {products[key]}")

# Iterating through values
print("\nIterating through values:")
for value in products.values():
    print(f"Value: {value}")

# Iterating through key-value pairs
print("\nIterating through key-value pairs:")
for key, value in products.items():
    print(f"Key: {key}, Value: {value}") # dict_items([(1, 'apples'), (3, 'melons'), ('name', 'Panos'), ('age', 30)])

# By iterating each key, value has these:
# [
#   (1, 'apples'), 
#   (3, 'melons'), 
#   ('name', 'Panos'), 
#   ('age', 30)
# ]
def print_cities(*cities):  # *cities -> unspecified No of city parameters (equivalent to ...cities in js)
    # Check if any cities are provided
    if not cities:
        print("No cities provided")
    else:
        # Join and print the cities separated by commas
        print("Cities:", ", ".join(cities)) # JS -> cities.join(", ")

def main():
    # Example calls to print_cities
    print_cities("Athens", "London", "Paris")  # Cities: Athens, London, Paris
    print_cities("Athens")  # Single city
    print_cities()  # No cities provided


# Ensure the script runs only when executed directly
# Every Python file has a built-in variable called __name__.
# When the file is run directly (e.g., python file.py), Python sets
# __name__ to "__main__".
# When the file is imported into another file, 
# __name__ becomes the filename (module name), not "__main__".
if __name__ == "__main__":
    print(__name__)
    main()
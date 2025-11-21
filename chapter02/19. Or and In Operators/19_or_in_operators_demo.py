choice = 'q'

# or
if choice == 'q' or choice == "Q":
    print("OK")
else:
    print("Not OK")

# upper
if choice.upper() == 'Q':
    print("OK")
else:
    print("Not OK")

# in (Pythonian!)
# more than Q, q, Quit, for example -> lalakis 
if choice in ('q', 'Q'):
        print("OK")
else:
    print("Not OK")
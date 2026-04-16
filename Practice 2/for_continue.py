# Use continue to skip one step
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue # Skip "banana" and go to the next item
    print(x)
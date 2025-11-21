# lists are use to store multiple items in a single variable

my_list = [10, 20, 40, 50]
print(my_list)

mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# accessing list items by their INDEX number
fruits = ["apple", 'banana', "cherry"]
print(fruits[0])
print(fruits[2])

# You can also use negative indexes to count from the end
print(fruits[-2])

# MODIFY th list
fruits[1] = "mango"
print(fruits)

# Adding to list
fruits.append("orange")
print(fruits)

fruits.insert(1, "kiwi")
print(fruits)

# removing items
fruits.remove("apple")
print(fruits)

fruits.pop()
print(fruits)

# Check if an item exist 
if "mango" in fruits:
    print("Yes, mango is in the list!")

# List length
print(len(fruits)) # number of items in the list
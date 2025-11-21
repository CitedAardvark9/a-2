# Sets are UNORDERED, UNINDEXED, and have NO DUPLICATE

fruits = {"apple", "banana", "cherry"}
print(fruits)

# NO DUPLICATES
fruits = {"apple", "banana", "apple"}
print(fruits)

# check if item exist
print("banana" in fruits)

# Add item
fruits.add("orange")
print(fruits)

# Add multiple items
fruits.update(["kiwi", "mango"])
print(fruits)

# remove item
fruits.remove("banana")
print(fruits)

# If you're not sure an item exists, use discard() to avoid errors
fruits.discard("papaya")
print(fruits)

# Set operations (like math)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))          # Combine both with no duplicates
print(set1.intersection(set2))   # Common elements
print(set1.difference(set2))     # Items in set1 but NOT in set2

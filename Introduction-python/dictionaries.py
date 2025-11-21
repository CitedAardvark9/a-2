# dictionaries store data in key value pairs

students = {
    "name": "Leo",
    "age: 22,"
    "major": "computer science"
}

print(students)

# accessing items
print(students["name"])      # Access by key 
print(students.get("major")) # Access another key

# add new item
students["graduation_year"] = 2025
print(students)

# Changing Values
students["age"] = 23
print(students)

# Remove item
students.pop("major")
print(students)

# Check if KEY exists
if "name" in students:
    print("Key 'name' is in the dictionary")

# Nested dictionary
students = {
    "student1": {"name": "leo", "age": 20},
    "student2": {"name": "alex", "age": 30}
}

print(students["student1"]["name"])  # Access nested value

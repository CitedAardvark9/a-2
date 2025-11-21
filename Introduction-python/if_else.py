# if -> checks a condition
# elif -> checks another condition if previous ones are False
# else -> runs only if all conditions above are False

x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


# short-hand if statement (single line)
if x > 5: print("x is greater than 5")


# Checking multiple conditions
age = 17
if age >= 18:
    print("You’re an adult")
elif 13 <= age < 18:
    print("You’re a teenager")
else:
    print("You’re a child")


# Using logical operators (and/or/not)
temp = 72
if temp > 60 and temp < 80:
    print("Comfortable weather")

if temp < 50 or temp > 90:
    print("Extreme temperature alert!")


# Nested if statements (if inside an if)
score = 92
if score >= 90:
    print("A grade")
    if score > 95:
        print("…and you aced it!")
else:
    print("Below an A")


# Comparing strings
mood = "happy"
if mood == "happy":
    print("Keep that energy!")
elif mood == "sad":
    print("Hope things get better.")
else:
    print("Mood unclear, deploying snacks.")


# Using "in" for membership tests
favorite = "apple"
if favorite in ["apple", "banana", "grape"]:
    print("That’s a fruit I know!")
else:
    print("Exotic choice!")

# Shorthand ternary operator
age = 20
status = "adult" if age >= 18 else "minor"
print(status)


# Checking if a value exists
username = ""
if username:
    print("Username set.")
else:
    print("Username missing!")


# Practical numeric classification
num = -3
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")


# MINI CHALLENGE IF_else
# Create a file called if_grade.py

# 1. Ask the user to enter a number from 1–100 and store it in a variable called "score"
score = int(input("Enter your score (1-100): "))

# 2–5. Determine the grade using if / elif / else
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# 6. Create a variable "passed" – True if score >= 70, otherwise False
passed = True if score >= 70 else False

# 7. If passed is True, print "congratulations!", otherwise print "Try Again!!!"
if passed:
    print("congratulations!")
else:
    print("Try Again!!!")

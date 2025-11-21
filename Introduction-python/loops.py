# ---------------------------------------------
# Loops Cheat Sheet
# ---------------------------------------------
# Loops let you repeat blocks of code.
# Python has two main loops: for-loops and while-loops.
#
# for-loop → iterates over something (list, string, range, etc.)
# while-loop → repeats while a condition is True


# ---------------------------------------------
# For Loops
# ---------------------------------------------

# Basic for loop
for i in range(5):
    print(i)          # prints 0,1,2,3,4


# Looping through a list
fruits = ["apple", "banana", "grape"]
for f in fruits:
    print(f)


# Looping with index (enumerate)
for index, item in enumerate(fruits):
    print(index, item)


# Looping through a string
for char in "Python":
    print(char)


# Looping through a dictionary
grades = {"Alice": 90, "Bob": 82, "Chris": 76}

for name, score in grades.items():
    print(name, score)


# Using range(start, stop, step)
for n in range(10, 0, -2):
    print(n)          # 10, 8, 6, 4, 2


# ---------------------------------------------
# While Loops
# ---------------------------------------------

# Basic while loop
count = 0
while count < 5:
    print("count is", count)
    count += 1


# Using break (force-stop the loop)
num = 1
while True:           # infinite loop until break
    if num > 5:
        break
    print(num)
    num += 1


# Using continue (skip to next iteration)
for i in range(10):
    if i % 2 == 0:
        continue      # skips even numbers
    print("Odd number:", i)


# ---------------------------------------------
# Nested Loops (loop inside a loop)
# ---------------------------------------------

for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")


# ---------------------------------------------
# Looping with else
# ---------------------------------------------
# The else block runs only if the loop finishes normally
# (not stopped by a break)

for n in range(1, 6):
    if n == 3:
        break
else:
    print("Loop finished with NO break!")

# since break happened, else does NOT run


# ---------------------------------------------
# Common Practical Patterns
# ---------------------------------------------

# Summing numbers
total = 0
for n in range(1, 6):
    total += n
print("Total:", total)


# Searching for something
nums = [4, 8, 2, 9, 1]
found = False

for n in nums:
    if n == 9:
        found = True
        break

if found:
    print("Found 9!")
else:
    print("9 not found")


# Building a new list with a loop
squares = []
for n in range(1, 6):
    squares.append(n * n)

print(squares)


# List comprehension (advanced compact version)
squares2 = [n * n for n in range(1, 6)]
print(squares2)

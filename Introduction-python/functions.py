# ---------------------------------------------
# Functions
# ---------------------------------------------
# A function is a reusable block of code.
# You "define" it once, and you can "call" it many times.
#
# Syntax:
# def function_name(parameters):
#     code to run
#
# Functions help keep code organized, reduce repetition,
# and make programs easier to update or expand.



# Basic function (no parameters)
def greet():
    print("Hello there!")

greet()   # calling the function



# Function with parameters (inputs)
def greet_user(name):
    print("Hello,", name)

greet_user("Robert")
greet_user("Alice")



# Function with multiple parameters
def add(a, b):
    result = a + b
    print("Sum:", result)

add(3, 7)



# Function that RETURNS a value instead of printing
def multiply(a, b):
    return a * b

product = multiply(6, 8)
print("Result:", product)



# Returning multiple values
def analyze_number(n):
    return n * 2, n ** 2, n % 2

double, square, remainder = analyze_number(5)
print(double, square, remainder)



# Default parameter values
def welcome(name="friend"):
    print("Welcome,", name)

welcome()          # uses default
welcome("Sarah")   # overrides default



# Keyword arguments (more readable)
def order(item, size, topping):
    print(f"Order: {size} {item} with {topping}")

order(item="pizza", size="large", topping="mushrooms")



# Functions with *args (variable number of arguments)
def total_cost(*prices):
    return sum(prices)

print(total_cost(4.99, 2.50, 3.00, 9.99))



# Functions with **kwargs (variable named arguments)
def display_profile(**info):
    for key, value in info.items():
        print(key, ":", value)

display_profile(name="Alex", age=29, job="Developer")



# Function with docstring (description)
def square(x):
    """Returns the square of a number."""
    return x * x

print(square.__doc__)  # prints the docstring



# Nested functions (a function inside another)
def outer():
    print("Outer running")

    def inner():
        print("Inner running")

    inner()

outer()



# Function as a value (you can store or pass it)
def shout(msg):
    return msg.upper()

def whisper(msg):
    return msg.lower()

def communicate(fn, message):
    print(fn(message))

communicate(shout, "Hello!")
communicate(whisper, "Hello!")


# Mini Challenge: Subtraction Function

# 1. Create a function called subtraction
# 2. The function needs to have 2 parameters
def subtraction(a, b):
    return a - b

# 3. Assign the function call to a variable and pass two numbers
result = subtraction(10, 3)

# 4. Print the variable
print(result)   # should print 7

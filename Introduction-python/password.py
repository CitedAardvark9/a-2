# MINI CHALLENGE: PASSWORD CHECKER
# Create a file called password.py

# 1. Ask the user to enter a password
password = input("Enter password: ")

# correct password to check against
correct = "secret123"

# 2–3. Keep asking until the user gets it right
while password != correct:
    print("WRONG! Try Again!")
    password = input("Enter password: ")

# 4. If correct, print access message
print("Access Granted!")

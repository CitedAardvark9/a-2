# MINI CHALLENGE: Count how many words have 5 or more letters
# Create a file called letters.py

# 1. Create a list with some words
words = ["python", "cat", "banana", "loop", "science", "code"]

# 2. Use a for loop to go through each word
count = 0

for w in words:
    # 3. Count how many words have 5 or more letters
    if len(w) >= 5:
        count += 1

# 4. Print the result
print("Number of words with 5 or more letters:", count)

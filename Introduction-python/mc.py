# MINI CHALLENGE: STUDENT REPORT CARD

# 1. Create the dictionary
report_card = {
    "name": "Leo",
    "subject": "Mathematics",
    "grades": [85, 92, 78]
}

# 2. Print student's name and subject
print("Name:", report_card["name"])
print("Subject:", report_card["subject"])

# 3. Calculate the average of the 3 grades
average_grade = sum(report_card["grades"]) / len(report_card["grades"])

# 4. Add the average to the dictionary
report_card["average"] = average_grade

# 5. Conditional message based on the average
if average_grade >= 90:
    print("excellent")
elif 70 <= average_grade <= 89:
    print("good job")
else:
    print("needs improvement!")

# 6. Remove the "subject" key and print the updated dictionary
del report_card["subject"]

print(report_card)

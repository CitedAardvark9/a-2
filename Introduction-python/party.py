# MINI CHALLENGE: Party Guest List

# 1. Create two sets
invited_friends = {"Alex", "Sam", "Leo", "Mina"}
rsvped = {"Mina", "Sam", "Jordan"}

# 2. Print:
print(invited_friends.union(rsvped))        # Everyone who was invited (union)
print(invited_friends.intersection(rsvped)) # Everyone who said they're going (rsvped)
print(invited_friends.difference(rsvped))   # Those who haven't replied yet (difference)

# 3. Add two new names to invited_friends
invited_friends.update(["Chris", "Nora"])
print(invited_friends)

# 4. One person canceled – remove them from rsvped
rsvped.remove("Jordan")
print(rsvped)

# 5. Print how many total confirmed guests are attending
confirmed = invited_friends.intersection(rsvped)
print(len(confirmed))

# 6. Check if "Leo" is still coming
if "Leo" in rsvped:
    print("Leo is coming!")
else:
    print("Leo is NOT coming.")

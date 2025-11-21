# MINI CHALLENGE: The Travel Bag

# 1. Create a tuple called "travel_bag" with at least 5 items
travel_bag = ("shirt", "socks", "shoes", "charger", "toothbrush")

# 2. Print the SECOND and FOURTH items
print(travel_bag[1])  # socks
print(travel_bag[3])  # charger

# 3. Check if "shoes" is in your travel bag
if "shoes" in travel_bag:
    print("You are ready to walk!")
else:
    print("You forgot your shoes!!!")

# 4. Make a new tuple called "essentials" with 3 must-have items
essentials = ("wallet", "phone", "passport")

# 5. Combine both tuples into one called "final_bag"
final_bag = travel_bag + essentials

# 6. Print how many total items are now in final_bag
print(len(final_bag))

# 7. Print the last item in your final_bag
print(final_bag[-1])

#admission for anyone under 4 age is free
#addmission for anyone between the ages of 4 and 18 us $5
#admission for anyone age 18 or older is $10

age = 10

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("You admission cost is $10")

print("\n")
#Second way
if age < 4:
    price = 0
elif age <= 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")
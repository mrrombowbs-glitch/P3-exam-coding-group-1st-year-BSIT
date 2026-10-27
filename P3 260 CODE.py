print("Monthly Budget Calculator")
print("-------------------------")

allowance = float(input("Enter monthly allowance: "))
food = float(input("Enter food expense for 1 month: "))
rent = float(input("Enter rent expense: "))
transpo = float(input("Enter transportation expense: "))
electric = float(input("Enter electric bill: "))
water = float(input("Enter water bill: "))
other = float(input("Enter other expenses: "))

total = food + rent + transpo + electric + water + other
natira = allowance - total
per_day = natira / 30

# Budget per day breakdown
food_per_day = food / 30
transpo_per_day = transpo / 30
electric_per_day = electric / 30
water_per_day = water / 30

print("\n----- Monthly Result -----")
print("Monthly Allowance: ", allowance)
print("Food: ", food)
print("Rent: ", rent)
print("Transportation: ", transpo)
print("Electric: ", electric)
print("Water: ", water)
print("Other: ", other)
print("Total Expense: ", total)
print("Remaining Money: ", natira)
print("Remaining per day (30 days): ", per_day)

print("\n----- Budget Per Day (30 days) -----")
print("Food per day: ", food_per_day)
print("Transportation per day: ", transpo_per_day)
print("Electric per day: ", electric_per_day)
print("Water per day: ", water_per_day)
print("Remaining per day: ", per_day)

if natira > 0:
    print("\nYou still have savings.")
elif natira == 0:
    print("\nSakto lang budget mo.")
else:
    print("\nOver budget ka, kulang allowance mo.")
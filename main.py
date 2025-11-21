import math
print("Welcome to the tip calculator")
bills = float(input("What was the total bills?\n$"))
tip = int(input("how much tip would you like to give? 10, 15 0r 20?\n"))
split = int(input("How many people are splitting the bills?\n"))

total = bills + (bills *(tip/100))
per_person = total/split

print(f"Each person should pay: ${per_person:.2f}")































#!/usr/bin/env python3

# Question 1
import math
value1 = int(8.2)/int(2.1)
value2 = int(8.2/2.1)

if value1 == value2:
    print("int(8.2)/int(2.1) is the same as int(8.2/2.1)")
else:
    print("int(8.2)/int(2.1) is not the same as int(8.2/2.1)")

print("The solution of sqrt(678)/truncate(8.3/3) is", math.sqrt (678) // (8.3/3))

#Question 2
bill = float(input("Welcome to TipCalculator! Please input the bill amount: "))
tipYesNo = input("Would you like to tip? (yes/no) : ")
if tipYesNo == "yes":
    tipPercent = float(input("Please input how much you want to tip (in %): "))
    tipDollar = bill*(tipPercent/100)
    total = bill*((tipPercent/100)+1)
    print("The amount of tip is", round(tipDollar,2))
    print("The total bill amount is", round(total,2))
    print("Have a great day!")
elif tipYesNo == "no":
    print("Have a great day!")
else:
    print("Please type yes or no (note: it is case-sensitive)")

#Question 3
bank_balance="$250,000"

rate= float(input("What is the bank interest rate? (between 0.0 to 5.0 (in %)) "))
if rate > 5.0 or rate < 0.0:
    print("Please enter a number in the range of 0.0 to 5.0 and try again")
else:
    interest = float(bank_balance.replace(",","").replace("$","")) * (rate/100) / 12
    print ("Interest earned for this month is",round(interest,2))


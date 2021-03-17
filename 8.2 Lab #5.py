#!/usr/bin/env python3

# Question 1
bill = float(input("Welcome to TipCalculator! Please input the bill amount: "))
saidNo = False
while saidNo == False:
    tipYesNo = input("Would you like to tip? (yes/no) : ")
    if tipYesNo == "yes" or tipYesNo ==  "Yes" or tipYesNo == "YES" or tipYesNo == "Y" or tipYesNo == "y":
        saidNo = True
    else:
        print("IT IS REQUIRED TO SAY YES.")

tipPercent = float(input("Please input how much you want to tip (in %): "))
tipDollar = bill*(tipPercent/100)
total = bill*((tipPercent/100)+1)
print("The amount of tip is", round(tipDollar,2))
print("The total bill amount is", round(total,2))
print("Have a great day!")

# Question 2
tuition = 3000
for i in range(6):
    print("Year",i,"costs",round(tuition,2))
    tuition*=1.05

# Question 3
starting = 0.01
days = int(input("Enter the amount of days: "))
for i in range(days):
    print("Day",i+1,":       ",starting)
    starting*=2

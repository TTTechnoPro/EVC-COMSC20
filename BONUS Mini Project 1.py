#!/usr/bin/env python3
import random

listOfNumber = (input("Please enter a series of integers separated by a comma (must not be less than 2 numbers): ").replace(" ", "").split(","))
if len(listOfNumber) < 2:
    print("You need to input 2 or more numbers into the list. Try again!")
    exit()
for i in range(len(listOfNumber)):
    try:
        listOfNumber[i] = int(listOfNumber[i])
    except:
        print("You did not enter a series of integers. Try again! ")
        exit()
    if(listOfNumber[i] == 0):
        print("Zero has been detected in this list! The Random Number Generator will not select 0 to prevent the program from dividing by 0 and crashing.")

random1 = random.randint(0,len(listOfNumber)-1)

value1 = listOfNumber[random1]
while value1 == 0:
    random1 = random.randint(0,len(listOfNumber)-1)
    value1 = listOfNumber[random1]

listOfNumber.pop(random1)


random2 = random.randint(0,len(listOfNumber)-1)

value2 = listOfNumber[random2]
while value2 == 0:
    random2 = random.randint(0,len(listOfNumber)-1)
    value2 = listOfNumber[random2]


print("The Random Number Generator has selected the number:", value1 ,"and", value2)
print("Addition:", value1,"+", value2, "=", value1+value2)
print("Subtraction:", value1,"-", value2, "=", value1-value2, "and", value2,"-",value1,"=",value2-value1)
print("Multiplication:", value1,"*", value2, "=", value1*value2)
print("Division:", value1,"/", value2, "=", value1/value2, "and", value2,"/",value1,"=",value2/value1)

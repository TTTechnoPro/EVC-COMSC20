#!/usr/bin/env python3

#Question 1
print("This is a program that will print out a rectangle ")
length=int(input("What is the length of your rectangle "))
width=int(input("What is the width of your rectangle? "))
pattern=input("What pattern do you want to use ")

for i in range(width):
    print(length*pattern)

#Question 2

import random
mainList = []
divisible2List = []
divisible3List = []
divisible10List = []

def Average (list):
    total = 0
    if len(list) == 0:
        return "No Average"
    else:
        for i in list:
            total += i
        return total/len(list)

for i in range (15):
    mainList.append(random.randint(1,100))

for i in mainList:
    if i%2==0:
        divisible2List.append(i)
    if i%3==0:
        divisible3List.append(i)
    if i%10==0:
        divisible10List.append(i)
print("Here is the list of numbers randomly generated", mainList)

print()

print("Here is a list of the numbers that are divisible by 2:", divisible2List)
print("Here is a list of the numbers that are divisible by 3:", divisible3List)
print("Here is a list of the numbers that are divisible by 10:", divisible10List)

print()

print("The average of the list of numbers that are divisible by 2 is",Average(divisible2List))
print("The average of the list of numbers that are divisible by 3 is",Average(divisible3List))
print("The average of the list of numbers that are divisible by 10 is",Average(divisible10List))

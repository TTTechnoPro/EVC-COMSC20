#!/usr/bin/env python3
# Question 1

userNumber = input("Please input an integer: ")
isNumeric = userNumber.isnumeric()
if isNumeric == True:
    userNumber = int(userNumber)
    if userNumber % 2 == 0:
        print("The number",userNumber,"is an even number.")
    else:
        print ("The number",userNumber,"is an odd number.")
else:
    print("You didn’t enter an integer.")
# Question 2
import random
one_count=0
two_count=0
three_count=0
four_count=0
five_count=0
six_count=0

for i in range(10):
    number=random.randint(1,6)
    if number == 1:
        one_count+=1
    elif number == 2:
        two_count +=1
    elif number == 3:
        three_count +=1
    elif number == 4:
        four_count +=1
    elif number == 5:
        five_count +=1
    else:
        six_count +=1
print("The number of times the dice landed on 1 is", one_count, "time(s)")
print("The number of times the dice landed on 2 is", two_count, "time(s)")
print("The number of times the dice landed on 3 is", three_count, "time(s)")
print("The number of times the dice landed on 4 is", four_count, "time(s)")
print("The number of times the dice landed on 5 is", five_count, "time(s)")
print("The number of times the dice landed on 6 is", six_count, "time(s)")

# Question 3
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
for i in months:
    print("One of the months of the year is " + i)

# Question 4
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in numbers:
    #Part A
    print(i)
for i in numbers:
    #Part B
    print(i,i**2)

# Question 6
import turtle
screen = turtle.getscreen()
polygon = turtle.Turtle()

numOfSides = int(input("How many sides is the polygon? "))
lengthOfSides = int(input("How long is each side? "))
lineColor = input ("What is the color of the line? ")
fillColor = input ("What is the fill color of the line? ")

polygon.color(lineColor)
polygon.fillcolor(fillColor)
polygon.begin_fill()
for i in range(numOfSides):
    polygon.forward(lengthOfSides)
    polygon.lt(360/numOfSides)
polygon.end_fill()

# Question 11
import turtle
screen2 = turtle.getscreen()
art=turtle.Turtle()
art.hideturtle()
art.speed(20)
color = ["red","green","blue"]

for i in range(360):
    art.color(color[i%len(color)])
    art.fd(i)
    art.rt(100)


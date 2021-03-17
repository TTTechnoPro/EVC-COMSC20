#!/usr/bin/env python3

#Question 1
print("This is a program that will print out a triangle ")
base=int(input("What is the width of your triangle? "))
pattern=input("What pattern do you want to use ")

for i in range(base+1):
    print(i*pattern)

# #Question 2

import random

num1 = random.randrange(1000)
num2 = random.randrange(1000)
num3 = 9
operator = random.randint(0,3)
if operator == 0:
    print("What is " + str(num1) +  " + " + str(num2) +" ?")
    guess = int(input())
    if guess == num1+num2:
        print("Congratulations! That is correct!")
    else:
        print("Incorrect. Better luck next time")
elif operator ==1:
    print("What is " + str(num1) +  " - " + str(num2) +" ?")
    guess = int(input())
    if guess == num1-num2:
        print("Congratulations! That is correct!")
    else:
        print("Incorrect. Better luck next time")
elif operator ==2:
    print("What is " + str(num1) +  " * " + str(num2) +" ?")
    guess = int(input())
    if guess == num1*num2:
        print("Congratulations! That is correct!")
    else:
        print("Incorrect. Better luck next time")
elif operator ==3:
    print("What is " + str(num1) +  " / " + str(num2) +" ?")
    guess = int(input())
    if guess == num1/num2:
        print("Congratulations! That is correct!")
    else:
        print("Incorrect. Better luck next time")

#Question 8.14.1

def newtonSqrt(n):
    originalEstimate = 0.5 * n
    betterEstimate = 0.5 * (originalEstimate + n/originalEstimate)
    while betterEstimate != originalEstimate:
        originalEstimate = betterEstimate
        betterEstimate = 0.5 * (originalEstimate + n/originalEstimate)
        print("Approximately:", betterEstimate)
    return originalEstimate


print("Final Estimation:", newtonSqrt(25))

#Question 8.14.2

def print_triangular_numbers(n):
    triangleSum = 0
    for i in range(1,n+1):
        triangleSum += i
        print(str(i) + "        " + str(triangleSum))

print(print_triangular_numbers(5))

#Question 8.14.3

def is_prime(n):
    for i in range(2,n):
        if n%i== 0:
            return False
    return True
print(is_prime(7))

#Question 8.14.4

import turtle
import random
screen = turtle.getscreen()
moving = turtle.Turtle()
for i in range (50):
    moving.forward(10)
    moving.left(random.randrange(-90,90))


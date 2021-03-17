#!/usr/bin/env python3

#Question 1:
import random

randomNum = random.randint(1,10)
hasBeenGuessed = False
print("A number from 1-10 has been randomly selected. Your goal is to try and guess the number.")
while hasBeenGuessed == False:

    guess = int(input("Please guess a number from 1 to 10: "))
    if guess != randomNum and guess > 0 and guess < 10:
        print("That is wrong. Please try again.")
    elif guess > 10 or guess <1:
        print("You did not enter a number between 1 to 10")
    else:
        print("That is the correct answer! Congrats!")
        hasBeenGuessed = True
print("Thanks for playing!")

#Question 2
n = int(input("Please enter a positive integer: "))
initalGuess = n/2
print("The inital guess of the square root is: ", initalGuess)
oldGuess = initalGuess
for i in range(5):
    newGuess = (1/2) * (oldGuess + n/oldGuess)
    print(newGuess)
    oldGuess = newGuess

#Question 7
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#Question 8
def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False

#Question 9
def is_odd2(n):
    if is_even(n) == False:
        return True
    else:
        return False

#Question 12
def is_LeapYear(n):
    if n%4 == 0:
        return True
    elif n%100==0 and n%400==0:
        return True
    else:
        return False

#!/usr/bin/env python3

#Question 1
# Here are the following python commands that worked.

# print ("hello world")
# print ('hello world')

# Here are the following python commands that did not work.
# print hello world - Syntax Error: Missing parentheses
# print “hello world” - Syntax Error: Missing parentheses
# print(hello world) - Syntax Error: Invalid Syntax


# print("hello world", end="!!!") — This command makes the terminal append the "!!!" after the "hello world".
# print("hello world","hello world") — This command makes the terminal print "hello world" twice.
# print("hello world","hello world", sep="0") — This command makes the terminal place a 0 when before it prints the 2nd "hello world"
# print("hello world"+"jack") — This command makes the terminal print "hello world" and "jack" together.

# The plus sign makes the print statment print more than one thing. The more + means the more things the terminal will prininitials.
# What are end and sep inside a print statement?
# The end and sep command inside a print statement do different things. The end command makes the terminal append what is in the end quotes.
# The sep command inside a print statement makes the terminal separate printing multiple strings what's in the sep quotes. It will print out what is in the quotes before it moves onto printing the next thing.


#Question 2

# A good variable name for storing the number of credits taken in Fall 2017 would be fallCredits2017.
# A bad variable name for storing the number of credits taken in Fall 2017 would be x (since it's too generic)
# A good but unforunately illegal variable name is 2017FallCredits
# Here are the rules for legal variable naming
# A variable must start with a letter or an underscore
# A variable cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores
# Variable names are case-sensitive.

# Question 3a
num = 20
for i in range(5):
    print(num)
    num += 2

# Question 3b
num2 = 7
for i in range(9):
    print(num2)
    num2 +=7

# Question 3c
num3 = 1000
for i in range(11):
    print(num3)
    num3 -= 100

# Question 4
import turtle
screen = turtle.getscreen()
initials = turtle.Turtle()

initials.rt(90)
initials.fd(100)
initials.lt(135)
initials.fd(100)
initials.lt(90)
initials.fd(100)
initials.lt(135)
initials.fd(50)
initials.penup()
initials.goto(100,0)
initials.fd(100)
initials.bk(100)
initials.pendown()
initials.fd(100)
initials.bk(140)
initials.left(45)
initials.fd(150)
initials.fd(50)
initials.lt(45)
initials.lt(90)
initials.fd(130)

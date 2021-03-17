#!/usr/bin/env python3

# Question 1
# Python is an interpreted language. I know this because Python immediately outputs, like when you launch Python in Shell mode. There isn't a wait time for the code to compile, it outputs the answer of 2+3 immediately in the Terminal.

# Question 2
# A syntax error is when Python can't execute the program because it is syntactically incorrect. An example of this would be forgetting to put quotation marks when declaring a string.
# A semantic error is when Python is able to execute the program successfully. However, the program will not do the right thing. An example of this is forgetting to divide by 100 when printing a percentage amount.

# Question 3
# The rules for a legal variable in Python include the variable name starting with a letter. Another rule for a legal variable is that it must not start with a number. On top of that, variable names are case sensitive.

# Question 4

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))

sum = x+y
difference = x-y
product = x*y
quotient = x/y
remainder = x%y

print("The sum of the 2 numbers is", sum)
print("The difference of the 2 numbers is", difference)
print("The product of the 2 numbers is", product)
print("The quotient of the 2 numbers is", quotient, "and the remiander is ", remainder)
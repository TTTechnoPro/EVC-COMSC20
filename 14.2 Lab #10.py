#!/usr/bin/env python3

#Question 1
total = 0.0
try:
    infile = open('sales_data.txt', 'r')
    for line in infile:
        amount = float(line)
        total += amount
    infile.close()
    print(format(total, ',.2f'))
except IOError:
    print("File not found. Please try again.")
except ValueError:
    print("File must contain only integers and floats.")

except:
    print("An error has occured.")

else:
    print(format(total, ',.2f'))

#Question 2
# Write a program that tries to open a file names.txt. If the file does not exist, output a warning message.
try:
    infile = open('file_names.txt', 'r')
except:
    print("The file could not be found. Please try again.")

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))

try:
    print(num1/num2)
except ZeroDivisionError:
    print("The second number was 0. You cannot divide by 0")

except:
    print("An error occured.")
#Question 3
'''
try:
    x = float ("abc123")
    print(x)
except IOError:
    print("This code caused an IOError.")
except ZeroDivisionError:
    print("This code caused a ZeroDivisionError.")
except:
    print("An error happened")
    print("The end.")
'''
#What's going to be printed out is "An error happened" and "The End". That's because it's a valueError and the except blocks don't have a statement for ValueErrors so it'll default to the regular except code block.

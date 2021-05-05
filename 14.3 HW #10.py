#!/usr/bin/env python3
#Question1
'''
ValueError
NameError
IOError
SyntaxError
TypeError
These are common exceptions
'''

# Write a Python class named Student with two attributes student_id, student_name.
# Add a new attribute student_class. Create a function to display the entire attribute and their values in Student class.

#Question 2
class Student:
    student_id = None
    student_name = None
    student_class = None

    def getAttributes():
        print("ID Number is:",student_id)
        print("Student Name is:",student_name)
        print("Class is", student_class)

#Question 3
f = open('numbers.txt','r')
numbers =f.read()
num = numbers.split()
total = 0.0

for i in num:
    total += float(i)
print("The average of the numbers in the file is", total/len(num))

#Question 4
try:
    f = open('numbers.txt','r')
    numbers =f.read()
    num = numbers.split()
    total = 0.0

    for i in num:
        total += float(i)
    print("The average of the numbers in the file is", total/len(num))
except IOError:
    print("The file could not be found. Please try again")
except ValueError:
    print("The file should only contain integers and floats. Please try again")
except:
    print("An error has occured.")
'''
Something that will trigger an IOError is if the file is not present or if the filename is mistyped
Something that will trigger a ValueError is if there's a string in the file.
'''


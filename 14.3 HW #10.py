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


#Question 2
class Student:

    def __init__(student_id, student_name,student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def set_student_id (self,student_id):
        self.__student_id = student_id
    def set_student_name (self,student_name):
        self.__student_name = student_name
    def set_student_class (self,student_class):
        self.__student_class = student_class

    def get_student_id(self):
        return self.__student_id
    def get_student_name(self):
        return self.__student_name
    def get_student_class(self):
        return self.__student_class

    def __str__(self):
        return "ID: " + self.__student_id + \
            "\nName: " + self.__student_name + \
            "\nClass" + self.__student_class

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


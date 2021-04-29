# Question 1
'''
An example of an IOError occuring is when you open a file that doesn't exist (not found in Python3).
try:
    f = open("hello.txt", 'r')
except IOError:
    print("This file does not exist. Try again")


An example of a ValueError occuring is when you take the squareroot of -10.
try:
    import math
    math.sqrt(-10)
except ValueError:
    print("You cannot take the square root of negative numbers")


An example of a TypeError occuring is when you try to add an int and a str.
try:
    3+"str"
except TypeError:
    print("You can only add two things that are the same type.")


An example of a IndexError occuring is when you call index 6 when the list size is 5.
try:
    list=[2,3,4,5,6]
    list[6]
except IndexError:
    print("This index cannot be accessed since it's out of the range of the list")


An example of a KeyError occuring is when you try to access a key that isn't a dictionary.
try:
    hello = {1:"a"}
    hello[2]
except KeyError:
    print("The key cannot be accessed since it's not in the dictionary")


An example of a ZeroDivisionError occuring is when you try to divide by 0.
try:
    9/0
except ZeroDivisionError:
    print("You cannot divide by 0")


An example of a FileNotFoundError occuring is when the interpreter can't find the file (only in Python3).
try:
    f = open("hello.txt", 'r')
except FileNotFoundError:
    print("This file does not exist. Try again")


An example of a ImportError occuring is when the interpreter can't import the module.
try:
    import adlkfjls
except: ImportError
    print("IDE cannot import this library")
'''

#Question 2

article = "Python is often compared to other interpreted languages such as Java, JavaScript, Perl, Tcl, or Smalltalk. Comparisons to C++, Common Lisp and Scheme can also be enlightening. In this section I will briefly compare Python to each of these languages. These comparisons concentrate on language issues only. In practice, the choice of a programming language is often dictated by other real-world constraints such as cost, availability, training, and prior investment, or even emotional attachment. Since these aspects are highly variable, it seems a waste of time to consider them much for this comparison."
words = article.lower().replace(",","").replace(".","").split()
counter = dict()
for i in words:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
print(counter)


#!/usr/bin/env python3

# Chapter 10

# Question 1
'''
The reference diagram (line by line) is as follows:
Line 1 creates a list named a that contains 3 integers.
Line 2 creates a list named b that is copies the content of a entirely
Line 3 modifies the 0th element in the list and replaces it with the integer 5.
'''
# Question 3
myList = [76, 92.3, "hello", True, 4, 76]
myList.append("apple")
myList.append(76)
myList.insert(3,"cat")
myList.insert(0,99)
print(myList.index("hello"))
print(myList.count(76))
myList.remove(76)
myList.pop(myList.index(True))
print (myList)

# Question 5
def max(list):
    max = list[0]
    for i in range(1,len(list)):
        if list[i] > list[i-1] and list[i] > max:
            max = list[i]

    return max
print(max([-3,-24,-34,234285,-32,324,2349]))

# Question 11
def sumNotEven(list):
    exclude = 0
    total = 0
    for i in list:
        if i%2 ==0:
            exclude = i
            break
    for i in list:
        total += i
    return (total-exclude)
print(sumNotEven([3,4,3,3,3]))

# Question 12
def upToSam(list):
    number = list.index("sam")
    return (number+1)
print(upToSam(["yum","hello","barbers","sam","yucky"]))

# Question 17
import random
List = []
for i in range(100):
    List.append(random.randint(0, 1000))
print(List)

# Chapter 11

# Question 3
file = open("studentdata.txt", "r")

for aline in file:
    items = aline.split()
    for i in range(len(items[1:])):
        items[i+1] = int(items[i+1]
    print(items[0], "max is", max(items[1:]), "min is", min(items[1:]))

# Question 4
labdata = open("labdata.txt", "r")
num1 = 0
num2 = 0
for aline in labdata:
    values = aline.split()
    num1 += values[0]
    num2 += values [1]

    print((num2/20)+(m)*(value[0]-num1/20))

labdata.close()
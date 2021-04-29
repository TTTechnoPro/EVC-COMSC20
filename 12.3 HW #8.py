#!/usr/bin/env python3

# Question 1
def numberOfDigits(num):
    if type(num) == str or type(num) == float:
        print("You need to enter an int. Try again")
        exit()
    num = abs(num)
    counter = 1
    if num < 10:
        return 1

    while num/10 >= 1:
        num /= 10
        counter += 1
    return counter
print(numberOfDigits(-5))
# Question 2
def numberOfDigitsFloat(num):
    if type(num) == str:
        print("You need to enter an int or float. Try again")
        exit()
    num = abs(num)
    num = int(num)
    counter = 1
    if num < 10:
        return 1

    while num/10 >= 1:
        num /= 10
        counter += 1
    return counter
print(numberOfDigitsFloat(45.667))

# Question 3
import random
f = open("random_positive_numbers.txt", "w")
g = open("random_negative_numbers.txt", "w")
total1 = 0
total2 = 0
counter1 = 0
counter2 = 0
for i in range(50):

    number = random.randint(-20,20)
    if number >= 0:
        f.write(str(number)+"\n")
        total1 += number
        counter1 += 1

    else:
        g.write(str(number)+"\n")
        total2 += number
        counter2 += 1
f.write("The average of the positive numbers is "+ str(total1/counter1))
g.write("The average of the positive numbers is "+ str(total2/counter2))




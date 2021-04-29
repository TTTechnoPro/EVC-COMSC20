#!/usr/bin/env python3

# Question 1
import random
f = open("random_numbers.txt", "w")

for i in range(50):
    total = 0
    number = random.randint(-20,20)
    f.write(str(number)+"\n")
    total += number



# Question 2
f.write("The average of these 50 numbers is "+ str(total/50))
#!/usr/bin/env python3

#Question 1

import random
def Greetings (name):
    if name == "":
        name =  "Doc"
    greetingList = ["Hello","Dear","How are you,","What's up", "Good morning", "Good afternoon", "Good evening"]
    randomNum = random.randint(0,len(greetingList)-1)
    print(greetingList[randomNum],name)
    print("Nice to meet you. Have a nice day")
Greetings("Dylan")

#Question 2
def Average (num1,num2,num3):
    total = num1 + num2 + num3
    return(total/3)
print(Average(103,5102,2310))

#Question 3
def Farenheit (Celsius):
    return (9/5)* Celsius +32
print(Farenheit(34))

print("Celcius" + "        " + "Farenheit")
for i in range (41):
    print(i , "C", "          ", round(Farenheit(i),1),"F")
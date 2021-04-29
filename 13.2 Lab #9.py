#!/usr/bin/env python3

# Question 1
import random
def magic8ball ():
    input("Please ask a question: ")
    list = ["Yes", "No", "Maybe", "Try Again", "Never ask me again", "Yes and No", "I don't know", "Absolutely", "Sure?", "Try asking tomorrow"]
    print(random.choice(list))
magic8ball()

#Question 2
codes = {
"a": "$",
"b":"]",
"c":"?",
"d":".",
"e":"<",
"f":"=",
"g":"!",
"h":"@",
"i":"#",
"j":"%",
"k":"^",
"l":"&",
"m":"*",
"n":"(",
"o":")",
"p":"-",
"q":"_",
"r":"+",
"s":"~",
"t":"`",
"u":"|",
"v":"Œ",
"w":"‰",
"x":"±",
"y":"Ó",
"z":"Æ"
}
def encrypt (string):
    newstring = ""
    for i in string:
        newstring += codes[i]
    print(newstring)

encrypt("hello")

def get_keys(val):
    for key, value in codes.items():
         if val == value:
             return key
    return "key doesn't exist"

def decrypt (string):
    newstring = ""
    for i in string:
        newstring += get_keys(i)
    print (newstring)

decrypt("@<&&)")

#Question 3
phonenumber = {
    "John": "408-999-9000",
    "Peter": "408-677-1020",
    "Jenny": "408-228-1011"
}
def get_key(val):
    for key, value in phonenumber.items():
         if val == value:
             return key

    return "key doesn't exist"
list= []
list.append((get_key("408-999-9000")))
list.append((get_key("408-677-1020")))
list.append((get_key("408-228-1011")))
print(list)

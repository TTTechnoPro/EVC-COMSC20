#!/usr/bin/env python3

#Question 1
def longestValue (string):
    newString = ""
    startingoff = ""
    for i in string:
        if i>startingoff:
            newString += i
            startingoff = i
    return newString

# print(longestValue("abcdefgzab"))

#Question 2
def is_Palindrome (string):
    string = string.lower()
    counter = -1
    for i in string:
        if i != " ":
            if i == string[counter]:
                counter -= 1
                if counter < (0-len(string)):
                    counter = (0-len(string))
            else:
                return False

        if string[counter] == " ":
                counter -= 1

    return True
# print(is_Palindrome("Are we not drawn onward, we few, drawn onward to new era"))

#Question 3
def PreProcess (string):
    string = string.lower()
    realString = ""
    for i in string:
        if i.isalnum():
            realString += i

    return realString



phrase=input("Please enter a phrase: ")
new_phrase=PreProcess(phrase)
print(is_Palindrome(new_phrase))

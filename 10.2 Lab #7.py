#!/usr/bin/env python3

#Question 1
def sortedString (string):
    string = sorted(string)
    FinalString = "".join(string)
    return FinalString

print(sortedString("cat"))

#Question 2
def MeanMedian(list):
    total = 0;
    for i in list:
        total += i
    actualMean = total/len(list)

    length = len(list)
    if length % 2 == 0:
        median1 = list[length//2]
        median2 = list[length//2 - 1]
        median = (median1 + median2)/2
    else:
        median = list[length//2]
    return (actualMean,median)

print(MeanMedian([1,2,9]))

#Question 3
def averageList(list):
    total = 0;
    for i in list:
        total += i
    average = total/len(list)
    return average
print(averageList([1,2,9]))

#Question 4
def AvgChar(list):
    total = 0;
    if len(list) % 2 == 0:
        for i in list:
            total += ord(i)
        letter = round(total/len(list))
        return(chr(letter))
    else:
        return list[len(list)//2]
print(AvgChar(["a","b","c","d","e"]))


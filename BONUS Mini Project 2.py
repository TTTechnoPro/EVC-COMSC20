#!/usr/bin/env python3

f = open("article.txt", "r", encoding = "ISO-8859-1")


text = f.read()
f.close()
words = text.split()

string = ""
for i in words:
    string += i
    string += " "


words = string.lower().replace(",","").replace("?","").replace(".","").replace("!","").replace("\x92s","").replace(":","").replace("\n","").split()
word_count = dict()
def build_dict(my_dict, article):
    if article in my_dict:
        my_dict[article] += 1
    else:
        my_dict[article] = 1

    return my_dict

def report_dict(my_dict):
    print("Total number of words is", sum(my_dict.values()), "and the most frequent word is:", max(word_count,key=word_count.get))

def update_dict(my_dict, article):
    if article in my_dict:
        my_dict[article] += 1
    else:
        my_dict[article] = 1
    print("The dictionary has been updated. The new word count is", sum(my_dict.values()))
    return my_dict


# Main Code
for i in words:
    build_dict(word_count, i)
report_dict(word_count)
update_dict(word_count, "hello")

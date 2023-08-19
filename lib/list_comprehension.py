#!/usr/bin/env python3

def return_evens(num_list):
    evenList = [x for x in num_list if x%2==0]
    return evenList
    

def make_exclamation(sentence_list):
    newStr = [sentence + "!" for sentence in sentence_list]
    return newStr

lists=[0, 1, 3, 5, 7, 8, 9]
listA = ["Hello", "I'm doing great", "Python is fun"]

print(make_exclamation(listA))
print(return_evens(lists))
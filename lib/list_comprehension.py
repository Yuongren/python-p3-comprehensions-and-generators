#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]
num_list = [12, 4, 3, 5, 7, 6, 8, 9]
result = return_evens(num_list)
print(result)

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
sentence_list = ["Come", "How are you"]
result = make_exclamation(sentence_list)
print(result)
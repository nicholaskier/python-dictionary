import json

data = json.load(open("data.json"))

def define(word):
    if word in data:
        return data[word]
    else:
        return "The word does not exist. Please double check it."


word = input("Enter word:")

print(define(word))
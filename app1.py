import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        confirm = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(word, data.keys())[0])
        if confirm == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif confirm == "N":
            return "If you say so..."
        else:
            return "We didn't understand your entry. Please try again."
    else:
        return "The word does not exist. Please double check it."

word = input("Enter word:")

output = define(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
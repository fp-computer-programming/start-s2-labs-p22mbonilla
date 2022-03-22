# Author MB 03/21/2022

words = ["word", "dog", "flute", "red", "Prep","swimming", "studying"]

def smash(lst):
    sent = ""
    for word in lst:
        if word != lst[-1]:
            sent += word + " "
        else:
            sent += word + "."
    print(sent)

smash(words)
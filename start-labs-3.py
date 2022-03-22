# Author MB 03/21/2022

def comes_after(st, l): 
    string = ""
    for i, x in enumerate(list(st)):
        if i != len(st) - 1:
            if x.lower() == l.lower() and st[i+1].isalpha():
                string += st[i+1]
    return string

print(comes_after())
# Author MB 03/21/2022

def double_every_other(lst):
    for i in range(1,len(lst),2):
        lst[i] *= 2
    return lst

print(double_every_other)
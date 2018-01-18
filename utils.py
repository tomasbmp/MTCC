import math
import copy as c

def confirm(c):
    if (c == 'y') or (c == 'Y'):
        return True
    return False

def binom(a, b):
    return math.factorial(a)/(math.factorial(b)*math.factorial(a - b))

# In: a list of lists; Out: a list with all the combinations of
# elements of each list

def listCombinations(lst):

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        lists = []
        for item in lst[0]:
            lists += [[item]]
        return lists

    top = lst[-1]

    finalLists = []
    for item in top:
        print(top)
        lists = recursiveListCombination(lst[:-1])
        for l in lists:
            l += [item]
        finalLists += lists

    return finalLists

colors = ['W', 'U', 'B', 'R', 'G']

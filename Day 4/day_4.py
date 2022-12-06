import re
import itertools as it

def star_1():
    filename = 'own_input'
    lines = open(filename).read().split('\n')
    sections = [[*map(int, re.split(r",|-", pair))] for pair in lines]
    return(sum([interval_overlap(section[:2], section[2:]) for section in sections]))

def star_2():
    filename = 'own_input'
    lines = open(filename).read().split('\n')
    sections = [[*map(int, re.split(r",|-", pair))] for pair in lines]
    return(len(sections) - sum([interval_exclusion(section[:2], section[2:]) for section in sections]))

def interval_overlap(first, second):
    return (first[0] >= second[0] and first[1] <= second[1]) | \
            (first[0] <= second[0] and first[1] >= second[1])

def interval_exclusion(first, second):
    return (max(first) < min(second)) | \
            (min(first) > max(second))

print("The result for the first star is: ", star_1())
print("The result for the second star is: ", star_2())


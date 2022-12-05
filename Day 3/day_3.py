import itertools as it
import operator

def alphabet_to_int(input_letter):
    alphabet_length = 26
    if(input_letter.islower()):
        return(ord(input_letter) - ord('a')) + 1
    else:
        return(ord(input_letter.lower()) - ord('a')) + alphabet_length + 1

def star_1():
    filename = 'own_input'
    rucksacks = open(filename).read().split('\n')
    rucksack_compartments = [[x[:len(x)//2], x[len(x)//2:]] for x in rucksacks]
    common_elements = [set(rucksack[0]) & set(rucksack[1]) for rucksack in rucksack_compartments]
    common_elements = list(map(list, common_elements))
    #! This could be reduced if the list from before was not nested
    return(sum(map(alphabet_to_int, it.chain(*common_elements)))) 

def star_2():
    filename = 'own_input'
    rucksacks = open(filename).read().split('\n')
    groups = list(zip(*[iter(rucksacks)]*3)) # list of tuples
    groups = list(map(list, groups)) # list of lists
    common_elements = [list(it.accumulate(map(set, group), func=operator.and_))[-1] for group in groups]
    common_elements = (list(map(list, common_elements)))
    return(sum(map(alphabet_to_int, it.chain(*common_elements)))) 


print("The result for the first star is: ", star_1())
print("The result for the second star is: ", star_2())

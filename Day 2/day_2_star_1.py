
def score(your_decision, opponent_decision, loses_to, correspondance):
    opp_numeric = correspondance[opponent_decision]
    yours_numeric = correspondance[your_decision]
    result = 0
    if (yours_numeric == opp_numeric): result = 3
    elif(loses_to[your_decision] != opponent_decision): result = 6
    return yours_numeric + result 

loses_to = {
    'X': 'B',
    'Y': 'C',
    'Z': 'A',
}

correspondance = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

filename = 'own_input'
lines = open(filename).read().split('\n')
plays = [x.split(' ') for x in lines]

print(sum([score(play[1], play[0], loses_to, correspondance) for play in plays]))



from itertools import combinations as c
def minion_game(string):
    Stuart_score = 0
    Kevin_score = 0
    list_of_combinations = []
    for i in range(1, len(string) + 1):
        list_connector = list(c(string, i))
        list_of_combinations = list_of_combinations + list_connector
    list_of_combinations = [list(tuples) for tuples in list_of_combinations]
    list_of_substrings = []
    for lists in list_of_combinations:
        if ''.join(lists) in string:
            list_of_substrings.append(''.join(lists))
    set_of_substrings = set(list_of_substrings)
    required_list = list(set_of_substrings)
    for lists in required_list:   
        x = ''.join(lists)
        if x[0] in 'AEIOU':
            Kevin_score = Kevin_score + frequency(x)
        else:
            Stuart_score = Stuart_score + frequency(x)
    if Stuart_score > Kevin_score:
        print("Stuart", Stuart_score)
    elif Kevin_score > Stuart_score:
        print("Kevin", Kevin_score)
    else:
        print("Draw")


def frequency(string):
    global s
    count = 0
    for i in range(len(s) - len(string) + 1):
        if s[i:i + len(string)] == string:
            count = count + 1                                        
    return count          

if __name__ == '__main__':
    s = input()
    minion_game(s)

from pprint import pprint
from copy import deepcopy
import random

from grammar import sample
from util import build_ast_dictionary

def retrieve(code, index):
    tag, code = code
    if index == 'total':
        return tag
    else:
        for i in index[:-1]:
            code = code[i][1]
        return code[index[-1]][0]

def insert(code, index, item):
    tag, subcode = code
    if index == 'total':
        return item
    else:
        for i in index[:-1]:
            subcode = subcode[i][1]
        subcode[index[-1]] = item
    return code


def select_pairs(selected):
    if len(selected) < 2:
        return []
    possible = set(range(len(selected)))
    pairs = []
    while len(possible) > 1:
        first = random.choice(list(possible))
        possible.remove(first)
        second = random.choice(list(possible))
        possible.remove(second)
        pairs.append((selected[first], selected[second]))
    return pairs

cross_coefficient = 0.5

def merge(pair):
    first, second = pair
    base = deepcopy(first)
    a = build_ast_dictionary(first)
    b = build_ast_dictionary(second)
    ast_keys = lambda d : set(((k, v[0]) for k, v in d.items()))
    shared_keys = set.union(ast_keys(a), ast_keys(b))
    if len(shared_keys) > 1:
        shared_keys.remove(('total', 'expression'))
        cross_portion = max(1, int(cross_coefficient * len(shared_keys)))
        crosses = random.sample(shared_keys, cross_portion)
        for key, _ in crosses:
            insert(base, key, retrieve(second, key))
        return base
    else:
        if random.random() > 0.5:
            return first
        else:
            return second

def crossover(selected):
    pairs = select_pairs(selected)
    return [merge(pair) for pair in pairs]

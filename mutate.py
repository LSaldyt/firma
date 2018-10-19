from pprint import pprint
import random

from grammar import sample

def build_mutation_dictionary(code, prefix=tuple(), d=None):
    if d is None:
        d = dict()

    if prefix == tuple():
        d['total'] = code
    else:
        d[prefix] = code
    tag, subcode = code
    if isinstance(subcode, list):
        for i, subitem in enumerate(subcode):
            build_mutation_dictionary(subitem, prefix=prefix + (i,), d=d)

    return d

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

def mutate(code):
    print('Mutation:')
    print('Before:')
    print(code)
    mutation_dict = build_mutation_dictionary(code)
    selected = random.choice(list(mutation_dict.keys()))
    tag = retrieve(code, selected)
    new = sample(tag)
    code = insert(code, selected, new)
    print('After:')
    print(code)
    return code

#!/usr/bin/env python3
import sys, random
from pprint import pprint

from grammar import generate, interpret
from crossover import crossover
from mutate import mutate

ERROR_SCORE = 1000

def evaluate(code, inputs, outputs):
    #print(code)
    evaluated = [interpret(code)(x) for x in inputs]
    #pprint(evaluated)
    evaluated = [item if item is not None else ERROR_SCORE for item in evaluated]
    return sum(abs(x-y) for x, y in zip(evaluated, outputs))

def f(x):
    return x * 2 + 1

#def f(x):
#    if x in {0, 1}:
#        return 1
#    else:
#        return f(x - 1) + f(x - 2)
#
#def f(x):
#    return 2 * x + 3 * x * x

def genetic(f):
    N = 1000
    x = 2
    select_p = 0.5
    mutate_chance = 0.01

    inputs = list(range(6))
    outputs = [f(x) for x in inputs]
    population = [generate() for i in range(N)]
    #results = [interpret(code)(x) for code in population]
    #pprint(results)

    while True:
        scores = [evaluate(code, inputs, outputs) for code in population]
        size = len(scores)
        selected_indices = list(sorted(range(size), key=lambda t : scores[t]))[:int(select_p * size)]
        selected = [population[i] for i in selected_indices]
        selected_scores = [scores[i] for i in selected_indices]
        if 0.0 in selected_scores:
            print('Selected:')
            pprint(selected[0])
            break
        crossover(selected)
        mutated = [mutate(code) if random.random() < mutate_chance else code for code in selected]
        population = [generate() for i in range(N)]

def main(args):
    genetic(f)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

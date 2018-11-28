from pprint import pprint
from random import choice, random, randint

operators = {'+' : lambda a, b : a + b,
             '-' : lambda a, b : a - b,
             '*' : lambda a, b : a * b,
             '/' : lambda a, b : a / b,
             '%' : lambda a, b : a % b}

def f():
    return 'f'

def atom():
    if random() > 0.5:
        return 'x'
    else:
        return randint(-10, 10)

def operator():
    return choice(list(operators.keys()))

def expression():
    chance = random()
    if chance > 0.9:
        return ['operator', 'expression', 'expression']
    #elif chance > 0.8:
    #    return ['f', 'expression']
    else:
        return ['operator', 'atom', 'atom']

grammar = {
    'atom' : atom,
    'operator' : operator,
    'expression' : expression,
    'f' : f
}

def sample(name):
    element = grammar[name]
    if isinstance(element, list):
        return (name, list(map(sample, element)))
    else:
        generated = element()
        if isinstance(generated, list):
            generated = list(map(sample, generated))
        return (name, generated)

def generate():
    return sample('expression')

def interpret(code):
    if isinstance(code, tuple):
        code = code[1]
    if isinstance(code, list):
        code = [t[1] for t in code]
    def f(x):
        try:
            if isinstance(code, list):
                head, *rest = code
                if head == 'if':
                    if interpret(rest[0])(x):
                        return interpret(rest[1])(x)
                    else:
                        return interpret(rest[2])(x)
                elif head == 'f':
                    return f(interpret(rest)(x))
                elif head in operators:
                    return operators[head](*map(lambda c : interpret(c)(x), rest))
            elif code == 'x':
                return x
            else:
                return int(code)
        except ZeroDivisionError:
            return 100000000
    return f

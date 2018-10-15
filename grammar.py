from pprint import pprint
from random import choice, random, randint

operators = {'+' : lambda a, b : a + b,
             '-' : lambda a, b : a - b,
             '*' : lambda a, b : a * b,
             '/' : lambda a, b : a / b,
             '%' : lambda a, b : a % b}

def atom():
    if random() > 0.5:
        return 'x'
    else:
        return randint(-10000, 10000)

def operator():
    return choice(list(operators.keys()))

grammar = {
        'atom' : atom,
        'operator' : operator,
        'expression' : ['operator', 'atom', 'atom']
}

def sample(element):
    element = grammar[element]
    if isinstance(element, list):
        return list(map(sample, element))
    else:
        return element()

def generate():
    return sample('expression')

def interpret(code):
    def f(x):
        try:
            if isinstance(code, list):
                head, *rest = code
                if head == 'if':
                    if interpret(rest[0])(x):
                        return interpret(rest[1])(x)
                    else:
                        return interpret(rest[2])(x)
                elif head in operators:
                    return operators[head](*map(lambda c : interpret(c)(x), rest))
            elif code == 'x':
                return x
            else:
                return int(code)
        except:
            pass
            #print('Code produced an error')
        return None
    return f

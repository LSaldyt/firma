from pprint import pprint
from random import choice

operators = {'+' : lambda a, b : a + b,
             '-' : lambda a, b : a - b,
             '*' : lambda a, b : a * b,
             '/' : lambda a, b : a / b,
             '%' : lambda a, b : a % b}

def atom():
    return choice(['x', 1, 2, 3, 4, 5])

def operator():
    return choice(list(operators.keys()))

def generate():
    return [operator(), atom(), atom()]

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

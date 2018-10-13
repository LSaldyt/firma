
def generate():
    return ['if', ['%', 'x', 2], 0, 1]

def interpret(code):
    def f(x):
        if isinstance(code, list):
            head, *rest = code
            if head == 'if':
                if interpret(rest[0])(x):
                    return interpret(rest[1])(x)
                else:
                    return interpret(rest[2])(x)
            elif head == '%':
                return interpret(rest[0])(x) % interpret(rest[1])(x)
        else:
            try:
                return int(code)
            except:
                return x
    return f

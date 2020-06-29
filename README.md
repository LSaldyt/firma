# Firma
Genetic algorithm defined on generic grammars, currently learns LISP functions ([anti-skynet weight](https://imgs.xkcd.com/comics/genetic_algorithms.png) included)
![anti-skynet weight](https://imgs.xkcd.com/comics/genetic_algorithms.png)

Firma defines a simple genetic algorithm which uses a traditional programming language grammar.
The current implementation generates LISP functions, but is written to use any programming language in principle. 
All that is needed for a new language both a generate() and an interpret() function, where generate() generates a random piece of code, and interpret() compiles and runs that code.

This project is based on my other project, [sence](github.com/LSaldyt/sence).

For example, suppose we want to learn the following function:
```
def f(x):
    return 2 * x + 1
```

The function `genetic(f)` in `genetic.py` can be used to learn it as follows:
```
genetic(f)
```

Resulting in the potential output:
```
grid {firma}: python genetic.py
Selected:
('expression',
 [('operator', '+'),
  ('expression', [('operator', '%'), ('atom', 'x'), ('atom', 6)]),
  ('expression', [('operator', '+'), ('atom', 1), ('atom', 'x')])])
```


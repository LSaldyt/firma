# Firma
Genetic algorithm defined on generic grammars for solving the program learning problem ([anti-skynet weight](https://imgs.xkcd.com/comics/genetic_algorithms.png) included)
![anti-skynet weight](https://imgs.xkcd.com/comics/genetic_algorithms.png)

Firma defines a simple genetic algorithm which uses a traditional programming language grammar.
The current implementation generates python code, but is written to use any programming language in principle. 
All that is needed for a new language both a generate() and an interpret() function, where generate() generates a random piece of code, and interpret() compiles and runs that code.

This project is based on my other project, [sence](github.com/LSaldyt/sence), which has a nice descriptive [poster](https://github.com/LSaldyt/sence/blob/master/FURI_poster.pdf). A paper describing the project in more depth is planned.


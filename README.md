# Brainfuck Interpreter In Batch

Its a brainfuck interpreter in batch! :D

You can learn more about brainfuck [here](https://esolangs.org/wiki/Brainfuck).

Brainfuck has been proven to be turing complete (In fact, it was created to be
 turing complete and to run on the smallest interpreter), meaning batch is
 turning complete too!

## Execute it!

Executing is easy:

    $ interpreter < examples/hello.bf > CON

Alternatively, you can input your own program into stdin followed by a empty
 line and a `CTRL + Z` keypress to input a EOF character and start the program:

    $ interpreter
	,.,.,.,.,.,.!Hello!
	^Z

## IMPORTANT

The input file must have `CRLF` line endings or the program will loop forever.

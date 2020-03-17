
===============================================================================

Name

	myshell - Python shell with file name completion and command line editing

===============================================================================

How to use

	path/myshell > [command] [argument]

===============================================================================

Description

	myshell is completely written in in Python. It acts as a
	normal terminal, used as shell script command processor
	and provies the user a number of convenient features for
	interactive use.

===============================================================================

How myshell works

	After the startup process is complete, myshell begins to
	read commands and prompt with the path in which the file
	is located. myshell repeatedly asks for command line
	input, which is broken and read into words. The shell
	reads this and executes each command in next line. 

===============================================================================

Operations

	myshell supports a series of internal commands and 
	operations.


> cd [target directory]

	Changes the current working directory to the 
	[target directory]. If the [directory] argument is not 
	present, the current working directory is presented.

> clr

	Takes no arguments. Clears the screen of the terminal.
	It does not erase any previous commands or command
	executions.

> dir [target directory]

	List the contects of chosen directory.

> environ

	Takes no arguments. Lists all the 
	environment strings.

> echo [comment]

	Displays the arguments/comments given. Note that
	multiple spaces/tabs may be reduced to a single 
	space.

> help [command]

Gives a description of the given command, [command]. If 
no arguments given, the user manual is displayed. The
user manual is displayed in blocks of 20 lines. When 
space bar is entered (spacebar key is pressed), the next
block of text is displayed

> pause

Takes no arguments. Pauses operation of the shell until
enter key is pressed the user.

> quit

takes no arguments exits the shell.

===============================================================================

Output redirection

The command line input:

> [programme name] [argument 1] [argument 2] [>] [output file]

will execute the programme, [programme name] with two
arguments into [output file] instead of the screen.
the redirection character [>] will overwrite the contents of 
the file. 

If the output file does not exist, The command will create
a new file in the current working directory.

If the output file does exits and is located in the
current working directory, the command will overwrite and
erase the contects of the file.

The command line input:

> [programme name] [argument 1] [argument 2] [>>] [output file]

Similar to the previous command, however the redirection
character [>>] will append the outputs to the output file.
Instead of overwriting it.

===============================================================================

Backgound execution of programmes 

An amperstand at end a command line input:

> [command] &

or

> [command] [argument] &

is for programs that takes exceeding amounts of time to
execute. The command with an amperstand makes the program run
in the background. The shell immediately returns to the 
command line prompt after launching the program, allowing to 
user to execute other commands. The output of the program 
with the amperstand will print the outputs when the 
execution is finished.

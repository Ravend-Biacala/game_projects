from cmd import Cmd
import os
import sys
import subprocess
from subprocess import Popen
from multiprocessing import * 
from threading import Thread

class MyPrompt(Cmd):

    def default(self, args):
        # The default function is the last function the shell will look at
        # If none of the other commands are used, the shell will look at here in the defaul funtion

        internal = ["dir", "environ", "echo", "help"]  # a list of the internal commands of output redirection
        args = args.split()
        pid = os.fork()
        # creating a new process
        if pid > 0:
            wpid = os.waitpid(pid, 0)
            # this makes sure we have a child process not a parent process
        else:
            try:
                if args[-1] == "&":
                    #this if statement is for the amperstand, i created a thread for the program to run in the background
                    Thread(target=self.ampstand,args=(args[:-1],)).start()
                    # this makes thread of the function located in line 174
                elif len(args) > 3:
                    #this if statement refers to the output redirection
                    if ">" in args[-2] or ">>" in args[-2]:
                        #this checks if we have the redirection character
                        if len(args) == 4:
                            #this statements checks if we have one arguement to redirect
                            redirect(args[:2], args[-1], args[-2])
                            #Redirect is the funciton in line 179 and is explain there
                        elif len(args) == 5:
                            #this statement checks if we have two arguements to redirect
                            redirect2(args[:2],[args[0], args[2]],args[-1], args[-2])
                            #redirect2 is the fuction in line 189 and is explained there
                else:
                    try:
                        subprocess.call(args)
                        #this like calls any other files that are not in my internal commands
                    except:
                        print("command not found")
                        #this exception is thrown where a command is not found 
            except Exception as e:
                print("command not found: " + args)

    def do_cd(self, args):
        #this is my cd command
        curr_dir = os.getcwd()

        if len(args) == 0:
            #this if statement checks if no argument is given. if so the current working directory is reported
            print(curr_dir+"\n")
        elif args != "..":
            #this if statement is to into a nested directory
            try:
                new_dir = curr_dir + "/" + args
                os.chdir(new_dir)
                print(new_dir+"\n")
            except:
                print("Directory not found\n")

        elif args == "..":
            #this else if statemet is to back a directory
            try:
                go_back = "/".join(curr_dir.split("/")[:-1])
                os.chdir(go_back)
                print(go_back)
            except:
                print("Unable to go any further\n")

        self.path()
        #this calls the path function located in line 177, this changed the path in the prompt

 
    def do_clr(self, args):
        #this function clears the screen
        line = args.split()
        if len(line) == 0:
            print("\33c")
        else:
            print("Incorrect use of command")

    def do_dir(self, args):
        #this function lists all files and directories in the CWD 
        curr_dir = os.getcwd()
        line = args.split()
        if len(line) == 3:
            #this if statement is for output redirection and checks for an argument to change directory
            #example: dir folder1 > output.txt
            if (">" in line[-2] or ">>" in line[-2]):
                #this statement checks for the redirection character
                try:
                    files = os.listdir(curr_dir + "/" + "".join(line[:-2]))
                    #the files variable checks if the directory exists if not it throws and exception and lists the contents of another directory
                    files = [i for i in files if i[0] != "."]
                    files = "\n".join(files)
                    redirect_internal(files, line[-1], line[-2])
                    #this redirection function puts files into the output file.
                    #this funtion is located in line 219
                except:
                    print("Dir: cannot access '"+ line[-3] +"': No such file or directory")
        elif len(line) == 2:
            #this if statement is for output redirection and outputs contents of the current directory into the output file
            #Example: dir > output file
            if (">" in line[-2] or ">>" in line[-2]):
                files = os.listdir(curr_dir)
                files = [i for i in files if i[0] != "."]
                files = "\n".join(files)
                redirect_internal(files, line[-1], line[-2])
                #this redirection function puts files into the output file.
                #this funtion is located in line 219         
        else:
            #this else statement is for regular command line input   
            if len(args) == 0:
            #this if statement is for if given no arguments and lists contents of the CWD
                files = os.listdir(curr_dir)
                for name in files:
                    if name[0] != ".":
                    #take away all the hidden files
                        print(name)
                print("")
            else:
            #this else statement is for if given arguments and lists contents of the another directory
            #Example: dir ..
                try:
                    #an exception is thrown if the directory is not found
                    files = os.listdir(curr_dir + "/" + args)
                    for name in files:
                        if name[0] != ".":
                        #This if statements gets rid of hidden files
                            print(name)
                    print("")
                except:
                    print("Directory not found\n")

    def do_environ(self, args):
        lst = os.environ
        line = args.split()
        if len(line) == 2:
            if (">" == line[-2] or ">>" == line[-2]):
                contents = []
                for key, value in lst.items():
                    contents.append(key)
                    contents.append(value)
                contents = "\n".join(contents)
                redirect_internal(contents, line[-1], line[-2])
        elif len(args) == 0:
            for key, value in lst.items():
               print("\n" + key + "\n" + value)

    def do_echo(self, args):
        line = args.split()
        if len(line) == 0:
            print("no arguments given")
        elif len(line) > 0:
            if len(line) > 2:
                if ">" == line[-2] or ">>" == line[-2]:
                    comment = " ".join(line[:-2])
                    redirect_internal(comment, line[-1], line[-2])
                else:
                    print(" ".join(line))
                    print("")
            else:
                print(" ".join(line))
                print("")

    def do_help(self, args):
        file = open("readme.txt", "r")
        line = args.split()
        if len(line) == 2:
            manual = file.read()
            redirect_internal(manual, line[-1], line[-2])
        else:
            print("")
    
            
            # man = file.read()
            # print(man)
            for k in range(25):
                man = file.readline().strip()
                print(man)
    
            i = 50
            while True:
                if i > 125:
                    break
                space = input()
                if space == " ":
                    for j in range(25):
                        man = file.readline().strip()
                        print(man)
                    i = i + 25

    def do_pause(self, args):
        if len(args) == 0: 
            pause = input()
        else:
            print("command doesn't exist")

    def emptyline(self):
        self.path()

    def do_quit(self, args):
        print("Quitting... see you later, dale is awesome\n")
        raise SystemExit

    def path(self):
        prompt.prompt = os.getcwd() + " > "

    def ampstand(self, args):
        subprocess.call(args)

def redirect(input1, output1, arrow):
    func = "w+"
    if arrow == ">>":
        func = "a"
    path = os.getcwd()+"/"+input1[0]
    out_file = open(output1, func) 
    p = Popen(input1, stdout=out_file, stdin=subprocess.PIPE, universal_newlines=True)
    output, errors = p.communicate()

def redirect2(input1, input2, output1, arrow):
    func = "w+"
    if arrow == ">>":
        func = "a"
    path = os.getcwd()+"/"+input1[0]
    out_file = open(output1, func)
    p1 = Popen(input1, stdout=out_file, stdin=subprocess.PIPE, universal_newlines=True)
    output, errors = p1.communicate()

    path = os.getcwd()+"/"+input2[0]
    out_file2 = open(output1, "a")
    p2 = Popen(input2, stdout=out_file2, stdin=subprocess.PIPE, universal_newlines=True)
    output, errors = p2.communicate()

def redirect_internal(input1, output1, arrow):
    func = "w"
    if arrow == ">>":
        func = "a"
    file = open(output1, func)
    file.write(input1)

    # if input1[0]=="echo":
    #     redirect(input1, output1, arrow)
    # elif input1[0] == "dir":
    #     redirect(["ls"]+input1[1:], output1, arrow)
    # else:
    #     redirect([input1[0]], output1, arrow)


def readfile(prompt):

    with open(sys.argv[1], "r") as f:
        args = [line.strip() for line in f.readlines()]
        prompt.cmdqueue = args

        if "quit" not in args:
            prompt.cmdqueue.append("quit")
    prompt.cmdloop()

if __name__ == "__main__":
    prompt = MyPrompt()
    if len(sys.argv) == 2:
        readfile(prompt)
    elif len(sys.argv) == 1:
        prompt.path()
        prompt.cmdloop("Starting prompt...")
    else:
        print("won't work")

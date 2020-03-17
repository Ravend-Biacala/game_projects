from cmd import Cmd
import os
import sys
import subprocess
from subprocess import Popen
from multiprocessing import * 
from threading import Thread

class MyPrompt(Cmd):

    def default(self, args):
        internal = ["dir", "environ", "echo", "help"]
        args = args.split()
        pid = os.fork()
        if pid > 0:
            wpid = os.waitpid(pid, 0)
        else:
            try:
                if args[-1] == "&":
                   Thread(target=self.ampstand,args=(args[:-1],)).start()
                   #return True
                elif len(args) > 3:
                    if ">" in args[-2] or ">>" in args[-2]:
                        if args[0] in internal:
                            redirect_internal(args[:-1], args[-1], args[-2])
                        elif len(args) == 4:
                            redirect(args[:2], args[-1], args[-2])
                            #print(args[:2])
                        elif len(args) == 5:
                            redirect2(args[:2],[args[0], args[2]],args[-1], args[-2])
                else:
                    try:
                        subprocess.call(args)
                    except:
                        print("command not found")
                #print("hello")
            except Exception as e:
                print("command not found: " + args)
        # except:
        #     print("Invalid Command")

    def do_cd(self, args):
        curr_dir = os.getcwd()

        if len(args) == 0:
            print(curr_dir+"\n")
        elif args != "..":

            try:
                new_dir = curr_dir + "/" + args
                os.chdir(new_dir)
                print(new_dir+"\n")
            except Exception:
                print("Directory not found\n")

        elif args == "..":

            try:
                go_back = "/".join(curr_dir.split("/")[:-1])
                os.chdir(go_back)
                print(go_back)
            except:
                print("Unable to go any further\n")
        self.path()
 

    def do_clr(self, args):
        if len(args) == 0:
            os.system("clear")

    def do_dir(self, args):
        curr_dir = os.getcwd()
        line = args.split()
        if len(line) == 3:
            if (">" in line[-2] or ">>" in line[-2]):
                try:
                    files = os.listdir(curr_dir + "/" + "".join(line[:-2]))
                #print(files)
                    redirect_internal(("dir "+args).split()[:-2], line[-1], line[-2])
                except:
                    print("Dir: cannot access '"+ line[-3] +"': No such file or directory")
        elif len(line) == 2:
            redirect_internal(["dir"], line[-1], line[-2])
                

        else:   
            if len(args) == 0:  
                files = os.listdir(curr_dir)
                for name in files:
                    if name[0] != ".":        # take away all the hidden files
                        print(name)
                print("")
            else:
                try:
                    files = os.listdir(curr_dir + "/" + args)
                    for name in files:
                        if name[0] != ".":
                            print(name)
                    print("")
                except:
                    print("Directory not found\n")

    def do_environ(self, args):
        limit = 10
        line = args.split()
        if len(line) == 2:
            if (">" == line[-2] or ">>" == line[-2]):
                redirect_internal(["env"], line[-1], line[-2])
        elif len(args) == 0:
            lst = os.environ
            for key, value in lst.items():
               print("\n" + key + "\n" + value)

    def do_echo(self, args):
        line = args.split()
        if len(line) == 0:
            print("no arguments given")
        elif len(line) > 0:
            if len(line) > 2:
                if ">" == line[-2] or ">>" == line[-2]:
                    redirect_internal(("echo "+args).split()[:-2], line[-1], line[-2])
                else:
                    print(" ".join(line))
                    print("")
            else:
                print(" ".join(line))
                print("")



    def do_help(self, args):
        file = open("readme.txt", "r")
        
        while True:
            
            for i in range:
                man = file.readline().strip()
                print(man)


    def do_pause(self, args):
        if len(args) == 0: 
            pause = input()
        else:
            print("command doesn't exist")

    def emptyline(self):
        self.path()

    # def limit(self, num):
    #     print("Press space to see the next 10")
    #     while True:
    #         space = input()
    #         if space == " ":
    #             return 0
    #             break
    #         print("press only space")

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
    if input1[0]=="echo":
        redirect(input1, output1, arrow)
    elif input1[0] == "dir":
        redirect(["ls"]+input1[1:], output1, arrow)
    else:
        redirect([input1[0]], output1, arrow)


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

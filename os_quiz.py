import sys

def answer(num):
	d = {
	0: "a",
	1: "a",
	2: "d",
	3: "c",
	4: "c",
	5: "d",
	6: "b",
	7: "c",
	8: "d",
	9: "a",
	10: "b",
	11: "b",
	12: "b",
	13: "c",
	14: "b",
	15: "b",
	16: "c",
	17: "c",
	18: "c",
	19: "a",
	20: "b",
	21: "a",
	22: "c",
	23: "d"
	}
	return d[num]

def questions(num):
	lst = [
		["The command to rename a file in Linux is:\na. mv \nb. ren \nc. cp \nd. cp -rename" ],
		["Embedded computers typically run on a ____ operating system.\na. Real Time\nb. Windows XP\nc. Network\nd. Cluster"],
		["Which part of a process contains temporary data such as function parameters, return addresses, and local variables?\na. text section\nb. data section\nc. program counter\nd. stack"],
		["Which of the following would lead you to believe that a given system is an SMP-type system?\na. Each processor is assigned a specific task.\nb. There is a boss–worker relationship between the processors.\nc. Each processor performs all tasks within the operating system.\nd. None of the above"],
		["What does the following command do:\nls -lR\n\na. Lists all files in the current directory\nb. Provides a long (detailed) list of files in the current directory Incorrect\nc. Provides a long (detailed) list of all contents of the current directory, and all sub directories\nd. Lists only directories in the current directory"],
		["A process may transition to the Ready state by which of the following actions?\na. Completion of an I/O event\nb. Awaiting its turn on the CPU\nc. Newly-admitted process\nd. All of the Above"],
		["The most common secondary storage device is:\na. Random Access Memory\nb. Hard Disks\nc. Tape drives\nd. Cloud Storage."],
		["What statement concerning privileged instructions is considered false?\na. They may cause harm to the system.\nb. They can only be executed in kernel mode.\nc. They cannot be attempted from user mode.\nd. They are used to manage interrupts."],
		["The two separate modes of operating in a system area. supervisor mode and system mode\nb. kernel mode and privileged mode\nc. physical mode and logical mode\nd. user mode and kernel mode."],
		["Which of the following is a property of peer-to-peer systems?\na. Clients and servers are not distinguished from one another.\nb. Separate machines act as either the client of the server but not both.\nc. They do not offer any advantages over traditional client-server systems.\nd. They suffer from the server acting as the bottleneck in performance."],
		["What is the Unit of time in a system?\na. Operating System\nb. A Process\nc. Timer\nd. mode bit."],
		["Which of The following refers to the number of processes in memory.\na. process count\nb. degree of multiprogramming\nc. long-term scheduler\nd. CPU scheduler"],
		["Which of the following statements concerning open source operating systems is true?\na. Solaris is open source.\nb. Source code is freely available.\nc. They are always more secure than commercial, closed systems.\nd. All open source operating systems share the same set of goals."],
		["Which of the following saves the state of the currently running process and restores the state of the next process to run.\na. save-and-restore\nb. state switch\nc. context switch\nd. None of the above"],
		["What does the following command do:\n\nLS ../.\na. lists the current directory.\nb. lists the parent directory\nc. lists all child directories of the current one.\nd. None of the above."],
		["The list of processes waiting for a particular I/O device is called:\na. A standby queue\nb. A device queue.\nc. A ready queue\nd. An interrupt queue Feedback"],
		["A process control block:\na. stores the address of the next instruction to be processed by a different process\nb. determines which process is to be executed next.\nc. includes information on the process's state\nd. is an example of a process queue"],
		["The purpose of the OS module in Python is:\na. To provide a portable way of using operating system dependent functionality.\nb. To run a platform-independent Operating System\nc. To provide low-level Operating System Functionality to the Python Programmer.\nd. All of the Above"],
		["Which of the following statements is false?\na. Mobile devices must be concerned with power consumption.\nb. Mobile devices can provide features that are unavailable on desktop or laptop computers.\nc. The difference in storage capacity between a mobile device and laptop is shrinking.\nd. Mobile devices usually have fewer processing cores than a standard desktop computer."],
		["Which of the following operating systems is not open source?\na. Windows\nb. BSD UNIX\nc. Linux\nd. PCLinuxOS"],
		["Two important design issues for cache memory:\na. speed and volatility\nb. size and replacement policy Correct\nc. power consumption and reusability\nd. size and access privileges Feedback"],
		["A clustered system does one of the following:\na. gathers together multiple CPUs to accomplish computational work.\nb. is an operating system that provides file sharing across a network\nc. is used when rigid time requirements are present\nd. can only operate one application at a time"],
		["The correct command to enable the user, and nobody else to read, write and execute a file is:\na. chmod 644\nb. chmod 777\nc. chmod 700\nd. None of the above."],
		["What does the following command do:\na. confirms whether the file list.txt exists in the current directory\nb. Lists the contents of the file list.txt\nc. Lists the contents of the current directory and outputs them to the file list.txt as well as to the screen.\nd. Lists the contents of the current directory and outputs them to a file, but not the screen."]
	]
	return lst[num][0]

def main():
	wrong_ans = []

	print("This is a multiple choice quiz. Good Luck.\n")

	num = 0
	while num < 24:
		print("Question "+str(num+1)+":")
		print(questions(num))	#print question

		while True:		#check input if you input a b c or d
			ans = input()
			ans = ans.lower()
			if ans in "abcd":
				break
			print("please only input the letters a, b, c or d\n")
		print("")

		q_lst = questions(num).split("\n")
		q_ans = answer(num)
		print("")
		for a in q_lst:
			if a[0:2] == q_ans+".":
				q_ans = a


		if ans == answer(num):
			print("Correct!, The answer was")
		else:
			print("Wrong you Loser!, the answer was")
			wrong_ans.append("\n".join([("Question "+str(num)),q_lst[0],q_ans]))
		print(q_ans)
		print("")
		num +=1

	if len(wrong_ans) == 0:
		print("Congradulations, You got everything Correct")
	else:
		print("You got", 24-len(wrong_ans), "questions right\n")
		print("Your Wrong Answers Were-------------------------------------\n")

	for f in wrong_ans:
		print(f)
		print("")

	print("Tapos. Dale is awesome")

if __name__ == '__main__':
	main()

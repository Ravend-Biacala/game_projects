import sys

def allDone(word, guesses):
	count = 0
	for i in word:
		for j in guesses:
			if i == j:
				count = count + 1
				break
	if len(guesses) == 0:
		return False
	return count == len(word)


def show_letter(word, guesses):
	if len(guesses) == 0:
		show = "_"*(len(word))
		return show
	
	show = ""
	for i in word:
		if i == "-":
			show+= "-"
		elif i in guesses:
			show+= i
		else:
			show += "_"
	return show



def hangman(word):
	losing = [
		"   |   ",
		"   |   ",
		"  _|__",
		"  |X X|",
		"  |_X_|",
		"    * ",
		"   ---",
		" /|    |\\",
		"/ |    | \\",
		"  ------",
		"   |  |",
		"   |  |",
		"   |  |",
		"  --  --"
		]

	winner = [
		"  ____",
		"  |- -|",
		"  |_U_|",
		"    | ",
		"   ---",
		" /|    |\\",
		"/ |    | \\",
		"  ------",
		"   |  |",
		"   |  |",
		"   |  |",
		"  --  --",
		]
	attempts = 15
	letters_used = ""
	print("")
	print("You have " + str(attempts) + " attempts." )
	print("Your word is")
	show = show_letter(word, letters_used)
	old_show = show
	print(show)

	i = 1

	while True:
		if (allDone(word, letters_used)):
			print("Well Done, the word was " + word + ".")
			print('\n'.join(winner))
			break
		print("guess a letter")
		guess_letter = str(input())
		letters_used += guess_letter
		show = show_letter(word, letters_used)#

		if old_show == show:
			attempts -= 1
			print("You have " + str(attempts) + " attempts left." )
			print('\n'.join(losing[:i]))
			i += 1
		else:
			old_show = show
		if i == len(losing):
			print("YOU LOSE")
			print('\n'.join(losing[:i+1]))
			print("TRY AGAIN")
			break		
		print(show)



		
	print("The End")


#def hangman():
#
#
def main():
	#print(allDone("computing", "computing"))
	#print(show_letter("computing", "comp"))
	#print(show_letter("hello", "ho"))
	hangman("tommyhilfiger")
if __name__ == '__main__':
	main()

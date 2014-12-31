#Vincent Siu
#2014 07 10
#Alright Kids
#We're back in the game baby!
#Time to get on this hype
#Let's start out easy now

from sys import argv
from sys import exit
import os.path



if not os.path.isfile("OWLparsed.txt"):
	if not os.path.isfile("OWL.txt"):
		print """
		You need to create a file named \"OWL.txt\" in the current directory
		with words in the common english language on each line. The script will
		handle the rest.
		"""
	else:
		unparsedFile = open("OWL.txt", 'r')
		unparsedDictionary = unparsedFile.readlines()
		parsedFile = open("OWLparsed.txt", 'w')
		for line in unparsedDictionary:
			x = line.find(' ')
			if x == -1:
				word = line.rstrip()
			else:
				word = line[:x]
			word1 = word + '\n'
			parsedFile.write(word1)
		unparsedFile.close()
		parsedFile.close()

if len(argv) != 2:
	print """
	Usage: theSpellChecker.py <fileName>
	Reads the file, and prints a list of incorrect words
	"""
	#Some old comments:
	#"Needs an input of a .txt filename in the current directory, so the program can check all the words"
	#"Too many inputs. Please only provide the filename of the .txt file you want to spellcheck."
	exit()

fileToBeChecked = open(argv[1])
listOfLines = fileToBeChecked.readlines()
fileToBeChecked.close()

validWordFile = open("OWLparsed.txt", 'r')
validWordListunparsed = validWordFile.readlines()
validWordFile.close()

validWordList = []
for line in validWordListunparsed:
	validWordList.append(line.rstrip())

invalidWordList = []

for line in listOfLines:
	listOfWords = line.split()
	for word in listOfWords:
		word1 = word.strip(":;\"'/\[]#!?,.@$%^&*()_+")
		if (word1.upper() == "False"):
			continue
		else:
			parsedWord = word1.upper()
		if parsedWord.isdigit() == False: 
			found = 0
			for validWord in validWordList:
				if validWord == parsedWord:
					found = 1
					break
			if found == 0:
				invalidWordList.append(parsedWord)
print "List of invalid words: "
print invalidWordList


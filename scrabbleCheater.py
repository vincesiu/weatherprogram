#Vincent Siu
#Scrabble word things!
#Hooray!
#Finally, project time :3 
#2014/06/25

#We allow 1's to be blank tiles!! anything but space. because then code is needed b/c whitespace is ghey
blank_tile = '1'

#score dictionary
from sys import argv
import time

	orig_dict_scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
	         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
	         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
	         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
	         "x": 8, "z": 10}
	dict_scores = {}
	for key in orig_dict_scores:
		dict_scores[key.upper()] = orig_dict_scores[key]	

	file_pathway = 'wordList.txt'


def makeList(filepath):
	"""making a list of the words from our file"""
	wordList = []
	file_wordList = open(filepath, 'r')
	for line in file_wordList:
		wordList.append(line.rstrip())

	file_wordList.close()
	return wordList

#WARNING it has newlines at the end of each thing ugh i dislike memory usage
def makeListv2(filepath):
	"""making a list of the words from our file WARNING DOESNT WORK"""
	file_wordList = open(filepath, 'r')
	wordList = file_wordList.readlines()
	file_wordList.close()
	return wordList

def findCompatibleWordList(wordList, given_rack):
	found_list = []
	for word in wordList:
		isUsed = []
		for i in range(len(given_rack)): 
			isUsed.append(0)

		for i in range(len(word)):
			letterfound = 0
			for j in range(len(given_rack)):
				if (word[i] == given_rack[j] or given_rack[j] == blank_tile) & (isUsed[j] == 0):
					isUsed[j] = 1
					letterfound = 1
					break

			if letterfound == 0:
				break
			if i == (len(word) - 1 ):
				found_list.append(word)
	return found_list

def getScore(word):
	score = 0;
	for i in range(len(word)):
		score += dict_scores[word[i]]
	return score

def getScoreDict(wordList):
	scoreList = []
	for word in wordList:
		temp_dict = {}
		temp_dict["word"] = word
		temp_dict["score"] = getScore(word)
		scoreList.append(temp_dict)
	return scoreList

if __init__ == "__main__":
	start_time = time.time()	
	if len(argv) < 2:
		print "Please remember to provide a valid rack/string of characters."
		exit()
	elif len(argv) > 3:
		print "You provided too many inputs. Please input only one rack/string of characters."
		exit()	

	raw_rack = argv[1]
	given_rack = raw_rack.upper()	

	BigList = makeList(file_pathway)
	smallList = findCompatibleWordList(BigList, given_rack)
	scoreList = getScoreDict(smallList)	

	print smallList
	

	final = sorted(scoreList, key=lambda k: k['score'])	

	for i in range(len(final)):
		print "%s %s" %(final[len(final) - i - 1]['score'], final[len(final) - i - 1]['word'])	
	

	print("--- %s seconds ---" % (time.time() - start_time))
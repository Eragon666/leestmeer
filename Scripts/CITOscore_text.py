# -*- coding: utf-8 -*-

from collections import Counter
import sys, getopt, argparse, re, math

# This is the main function of the code which calculates the CITO scores
# for a text and returns them and their variables as a tuple

def mainCITO(text):

	# Instantiates various variables
	common = 'database/common.txt' #text file of common words (hardcoded)
	lettersCount = 0
	totLetters = 0
	totSentences = 0
	avgWords = 0
	totWords = 0
	avgLetters = 0
	allWords = ""

	# Loops through all sentences in the text, removes various punctuation marks
	# and counts the words and letters.
	sentences = text.splitlines()	
	for sentence in sentences:
		if sentence:
			wordCount = 0
			if sentence:
				totSentences += 1
			words = re.split('\s+',sentence)
			wordCount += len(words)
			for word in words:
				lettersCount = len(word)
				totLetters += lettersCount
				allWords += word + ' '
			totWords += wordCount
	
	# Count up all unique words and calculate the type-token-frequency
	uniqueWords = Counter(allWords.split())
	typeTokenFrequency = (len(uniqueWords) * 1.0) / totWords
	
	# Opens the text file of common words
	commonFile = open(common)
	commonText = commonFile.read()
	commonWords = re.split(',', commonText)
	totCommonWords = 0
	
	# Counts how many words in the text are common words
	for commonWord in commonWords:
		totCommonWords = totCommonWords + uniqueWords[commonWord]

	# Calculations for some of the variables in the CITO formulas
	# The '*1.0' are fixes for integer divisions
	freqCommonWords = (totCommonWords * 1.0) / (totWords*1.0) 
	avgWords = totWords/(totSentences * 1.0)
	avgLetters = totLetters/(totWords * 1.0)

	CLIB = round(46 - 6.603 * avgLetters + 0.474 * freqCommonWords - 0.365 * typeTokenFrequency + 1.425 * avgWords)
	CILT = round(105 - (114.49 + 0.28 * freqCommonWords - 12.33 * avgLetters))
	
	return (CLIB, CILT, avgLetters, freqCommonWords, typeTokenFrequency, avgWords)


# This function states the commandline arguments that are needed
# for the program to run.
# if __name__ == "__main__":
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument("-corpus", "--corpus", help="Textfile of corpus", default="input.txt")
# 	parser.add_argument("-output", "--output", help="Give the type of output, CLIB=CLIB score, CILT=CILT score, debug=info", default="debug")
# 	parser.add_argument("-common", "--common", help="Textfile of common words", default="common.txt")
# 	args = parser.parse_args()
# 	main(args.corpus, args.output, args.common)

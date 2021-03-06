# -*- coding: utf-8 -*-

from collections import Counter
import sys, getopt, re, math


# This is the main function of the code which calculates the AVI score
# for a body of text. It does this by first calculating the average
# number of words per sentence and the average number of syllables
# per word. These two numbers are used in the final equation that 
# computes the AVI score.
# This code is mostly unused in the final product implementation
# however it might still be used if it's decided that the AVI score
# should be more prominent later on.

def mainAVI(text):
	# Instantiates various variables
	wordCount = 0
	syllableCount = 0
	totWords = 0
	totSyllables = 0
	totSentences = 0
	avgWords = 0.0
	avgSyllables = 0.0

	# Loops over all sentences in the text and calculates the average amount
	# of syllables and words.
	sentences = text.splitlines()
	for sentence in sentences:
		if sentence:
			totSentences += 1
			words = re.split('\s',sentence)
			wordCount = len(words)
			for word in words:
				syllableCount = countSyllables(word)
				totSyllables += syllableCount
			totWords += wordCount
	avgWords = totWords / (totSentences*1.0)
	avgSyllables = totSyllables / (totWords*1.0)

	# The actual calculations of the AVI-score and subsequent AVI-age group
	aviScore = math.ceil(195 - (2 * avgWords) - (200/3*avgSyllables)-0.5)
	aviAge = calcAge(aviScore)

	return (aviScore,totWords,totSentences,aviAge)
		
#aviScore is used to calculate the AVI Age
def calcAge(aviScore):
	if 127 >= aviScore >= 123:
		return 1
	elif 123 >= aviScore >= 112:
		return 2
	elif 112 >= aviScore >= 108:
		return 3
	elif 108 >= aviScore >= 100:
		return 4
	elif 99 >= aviScore >= 94:
		return 5
	elif 93 >= aviScore >= 89:
		return 6
	elif 88 >= aviScore >= 84:
		return 7
	elif 83 >= aviScore >= 79:
		return 8
	elif 78 >= aviScore >= 74:
		return 9
	else:
		return 0


# This function is used in order to count the number of syllables a
# word contains. It does this by evaluating each letter in the word
# and calling isSyllable/2 with that letter and the one before it
def countSyllables(word):
	syllableCount = 0
	prevLetter = '0'
	for i in range(len(word)):
		if isSyllable(word[i], prevLetter):
			syllableCount += 1
		prevLetter = word[i]
	return syllableCount

# Checks if the current letter is the start of a syllable
# This is defined as being the case when the current letter is a vowel
# while the previous letter is not.
def isSyllable(curLetter, prevLetter):
	vowels = 'AIOEUY'
	if vowels.find(prevLetter.upper()) == -1:
		if not(vowels.find(curLetter.upper()) == -1):
			return True
	elif syllableExceptions(curLetter, prevLetter):
		return True	
	else:
		return False

# This function contains several exceptions in the dutch language that
# count as new syllables. Rather than being a vowel followed by a consonant,
# an 'A' following an 'E', as well as those letters with umlauts can denote a new syllable.
# The umlaut detection is non functional in this product due to 
# difficulties with encoding.
# Once fixed, the appropriate code can be uncommented to allow it to function again.
def syllableExceptions(curLetter, prevLetter):
	curLetter = curLetter.encode('utf-8')#.decode('latin-1')
	prevLetter = prevLetter.encode('utf-8')#.decode('latin-1')
	e = 'E'
	a = 'A'
# 	trema = 'ËÏ'
	if not(e.find(prevLetter.upper()) == -1):
		if not(a.find(curLetter.upper()) == -1):
			return  True	
# 	if not(trema.find(curLetter.upper()) == -1):
# 		return True
 	return False

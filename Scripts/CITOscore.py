# -*- coding: utf-8 -*-

from collections import Counter
import sys, getopt, argparse, re, math

# This is the main function of the code which calculates the CITO score

def main():
	outputFile = open('database\\averages', 'w+')
	# List = ['www.3fm.nl', 'www.360magazine.nl', 'www.bright.nl', 'www.kidsweek.nl', 'www.nos.nl', 'www.nrc.nl', 'www.politie.nl']
	List = ['www.politie.nl']
	for source in List:
		corpus = 'database\\' + source
		output = 'banaan'
		common = 'database\\common.txt'
		(CLIB, CILT, avgLetters, freqCommonWords, typeTokenFrequency, avgWords) = main2(corpus, output, common)
		outputFile.write(source + '\n')
		outputFile.write('CLIB: ' + str(CLIB) + '\n')
		outputFile.write('CILT: ' + str(CILT) + '\n')
		outputFile.write('avgLetters: ' + str(avgLetters) + '\n')
		outputFile.write('freqCommonWords: ' + str(freqCommonWords) + '\n')
		outputFile.write('typeTokenFrequency: ' + str(typeTokenFrequency) + '\n')
		outputFile.write('avgWords: ' + str(avgWords) + '\n')
def main2(corpus, output, common):
	try:
		file = open(corpus, mode='r')
		text = file.read()
		# text = text.replace('\.\n','\. ').replace('\n','')
		file.close()	
	except IOError:	
		print('Cannot open '+corpus)
		sys.exit()

	lettersCount = 0
	totLetters = 0
	totSentences = 0
	avgWords = 0
	totWords = 0
	avgLetters = 0
	allWords = ""
	# punc = re.compile(':|,|;')
	# text = punc.sub(text)
	# text = re.replace(':|,|;', '', text)
	sentences = text.splitlines()
	for sentence in sentences:
		sentence = sentence.replace(':|,|;', '')
		wordCount = 0
		if sentence:
			totSentences += 1

		words = re.split('\s+',sentence)
		wordCount += len(words)
		for word in words:
			lettersCount = countLetters(word)
			if (lettersCount > 0) & (output=='debug'):
				print(word + ': ' +  str(lettersCount))
			totLetters += lettersCount
			allWords += word + ' '
		totWords += wordCount
		# print(allWords)
		# allWords += words

	uniqueWords = Counter(allWords)
	# print(uniqueWords)
	typeTokenFrequency = len(uniqueWords) / totWords

	commonFile = open(common, encoding='utf-8', mode='r')
	commonText = commonFile.read()
	commonLines = commonText.splitlines()
	commonWords = re.split(',', commonText)
	totCommonWords = 0

	for commonWord in commonWords:
		if uniqueWords[commonWord] > 0:
			print(commonWord)
		totCommonWords += uniqueWords[commonWord]
	print('totCommonwords: ' + str(totCommonWords))
		
	freqCommonWords = totCommonWords / totWords

	if output=='debug':
		print(sentences)

	avgWords = totWords/totSentences
	avgLetters = totLetters/totWords

	if output=='debug':
		print('Average amount of words per sentence: ' + str(avgWords))
		print('Average amount of letters per word: ' + str(avgLetters))

	print(avgLetters)
	print(freqCommonWords)
	print(typeTokenFrequency)
	print(avgWords)
	CLIB = 46 - 6.603 * avgLetters + 0.474 * freqCommonWords - 0.365 * typeTokenFrequency + 1.425 * avgWords
	CILT = 105 - (114.49 + 0.28 * freqCommonWords - 12.33 * avgLetters)

# if output=='CLIB':
	print('CLIB: ' + str(CLIB))
	# return CLIB
# elif output=='CILT':
	print('CILT: ' + str(CILT))
	# return CILT
	return (CLIB, CILT, avgLetters, freqCommonWords, typeTokenFrequency, avgWords)


def countLetters(word):
	return len(word)


# This function states the commandline arguments that are needed
# for the program to run.
if __name__ == "__main__":
	# parser = argparse.ArgumentParser()
	# parser.add_argument("-corpus", "--corpus", help="Textfile of corpus", default="input.txt")
	# parser.add_argument("-output", "--output", help="Give the type of output, CLIB=CLIB score, CILT=CILT score, debug=info", default="debug")
	# parser.add_argument("-common", "--common", help="Textfile of common words", default="database\\common.txt")
	# args = parser.parse_args()
	# main(args.corpus, args.output, args.common)
	main()
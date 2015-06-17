from collections import Counter
from collections import OrderedDict
import sys, getopt, argparse, re, pickle
from itertools import permutations

# Prepares an already tagged corpus and creates N-Gram model
def main(corpus, n):
	file = open(corpus, 'r')
	text = file.read()
	file.close()
	words = prepareText(text, 3)
	nGrams = makeNgrams(3, words)
	if n == 3:
		del nGrams['</s> <s> <s>']
	c = Counter(nGrams)
	# print(c)
	file = open(corpus+'_nGrams', 'wb')
	pickle.dump(c,file)
	file.close()

	# print(len(c))
	# print(sum(c.values()))


	# file = open(corpus+'_nGrams', 'rb')
	# b = pickle.load(file)
	# file.close()

	# print(len(b))
	# print(sum(b.values()))
	# return nGrams


def prepareText(corpus, n):
	lines = corpus.splitlines()
	words = []
	for line in lines:
		if line:
			wordline = re.split(' ', line)
			i=0
			prepend = []
			while i < n-2:
				words.append('<s>')
				i += 1
			words.append('<s>')
			for x in wordline:
				if x:
					words.append(x)
			words.append('</s>')
	return words

#Function that makes n-grams out of 'words'.
def makeNgrams(n, words):
	nGrams = Counter([' '.join(words[i:i+n]) for i in range(len(words)-n+1)])
	return nGrams

# This function states the commandline arguments that are needed
# for the program to run.
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	# parser.add_argument("-corpus", "--corpus", help="File of corpus")
	parser.add_argument("-corpus", "--corpus", help="file")
	parser.add_argument("-n")
	#Name and location of the text file to be parsed
	args = parser.parse_args()
	main(args.corpus, args.n)
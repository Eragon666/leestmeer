# -*- coding: utf-8 -*-

from collections import Counter
import sys, argparse, re, pickle, math
import ngramProfiler_text
import ast

# This file calculates the text difference based on the POS Ngrams, between a corpus and a text.
# The first argument is the name of the corpus (e.g. database/www.kidsweek.nl_POS_nGrams)
# The second argument is a string containing the POS tagged words to be compared
def main(corpus,text):
	try:
		with open(corpus, 'rb') as f:

			# get corpus, is a list of tupples
			P1 = pickle.load(f)

			print 'Score of ', corpus
			print 'For ', text
			# analyze current text, returns counter
			P2 = ngramProfiler_text.main(text,3)

			return(calcDiffUw(P1, P2))
	except IOError: 
		print('Cannot open '+corpus)


def calcDiffUw(P1, P2):
	D = 0.0
	P2l = Counter(list(P2))
	P1l = Counter(list(P1))
	plusje = P2l + P1l

	intrsct = []

	# Find intersection between P1 and P2
	for x in P2l:
		if x in P1l:
			intrsct.append(x)

	intrsct = len(intrsct)
	print('intrsct:'+  str(intrsct))

	union = len(P1) + len(P2l)

	# Sorensen-Dice coefficient
	# D1 = (intrsct * 2.0) / union * 100
	# print('Sorensen-Dice coefficient:' + str(D1))

	# calculate resemblance with Jaccard index
	#D2 = (intrsct * 1.0) / union * 100
	#print 'jaccard index:', D2

	# calculate overlap coefficient
	D3 = (intrsct * 1.0) / min([len(P1),len(P2l)]) * 100
	print ('Overlap coefficient:' + str(D3))

	# calculate the Tversky index
	# D4 = (intrsct * 1.0) / (intrsct + (len(P1)-intrsct) + (len(P2l)-intrsct)) * 100
	# print ('Tversky index:' + str(D4))

	# calculate the weighted frequency with idf score
	# D5 = 0.0
	# for x in plusje:
	# 	if (P1[x] > 0) & (P2[x] > 0):
	# 	# print(((P1[x] - P2[x])/((P1[x] + P2[x])/2))**2)
	# 	# print((2*(P1[x] - P2[x]))/(P1[x] + P2[x]))
	# 		D5 += ((2*(P1[x] - P2[x]))/(P1[x] + P2[x]))**2
	# print('Weighted idf frequency sum: ' +str(D5))

	return D3


# This function states the commandline arguments that are needed
# for the program to run.
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-corpus", "--corpus", help="File of corpus")
	parser.add_argument("-text", "--text", help="Text as string")
	args = parser.parse_args()
	main(args.corpus,args.text)

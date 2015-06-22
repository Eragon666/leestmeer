# -*- coding: utf-8 -*-

from collections import Counter
from collections import OrderedDict
import sys, getopt, re, pickle
from itertools import permutations

def main():
	fm = pickle.load(open('database\\3fm_POS_nGrams', 'rb'))
	threesixty = pickle.load(open('database\\360_POS_nGrams', 'rb'))
	bright = pickle.load(open('database\\bright_POS_nGrams', 'rb'))
	kidsweek = pickle.load(open('database\\kidsweek_POS_nGrams', 'rb'))
	nos = pickle.load(open('database\\nos_POS_nGrams', 'rb'))
	nrc = pickle.load(open('database\\nrc_POS_nGrams', 'rb'))
	sevendays = pickle.load(open('database\\sevendays_POS_nGrams', 'rb'))
	List = [(fm,'3fm_POS_nGrams'), (threesixty, '360_POS_nGrams'), (bright, 'bright_POS_nGrams'), (kidsweek, 'kidsweek_POS_nGrams'), (nos, 'nos_POS_nGrams'), (nrc, 'nrc_POS_nGrams'), (sevendays, 'sevendays_POS_nGrams')]
	for source,name in List:
		for x in source:
			freq = 0
			for source,name in List:
				if source[x] > 0:
					freq += 1
			source[x] = source[x] * math.log10(7/freq)
		with open('database\\' +name + '_idf', 'rb') as f:
			pickle.dump(source, f, protocol=2)


# This function states the commandline arguments that are needed
# for the program to run.
if __name__ == "__main__":
	main()
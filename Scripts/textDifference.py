from collections import Counter
import sys, argparse, re
import ngramProfiler
import ast

def main(corpus):
	try:
		with open(corpus, 'r') as f:
			s = f.read()
			P1 = ast.literal_eval(s)
			P2 = ngramProfiler.main('Art Adj Adj Prep V V Adv Adj\nConj Prep Art Adj Adv Adv\nAdj Int Prep Pron V Art Prep Art Adj N\nNum N Prep Pron Adv',3)
	except IOError: 
		print('Cannot open '+corpus)


def calcDiff(P1, P2):
	D = 0
	union = P1 + P2
	for x in union:
		part is ((P1[x] - P2[x])/((P1[x] + P2[x])/2))**2
		D += part
	print(D)
	return D

# This function states the commandline arguments that are needed
# for the program to run.
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-corpus", "--corpus", help="File of corpus")
	# parser.add_argument("-text", "--text", help="Text as string")
	#Name and location of the text file to be parsed
	args = parser.parse_args()
	main(args.corpus)
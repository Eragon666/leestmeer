import textDifference


def main(paragraph):
	print('3fm score:')
	textDifference.main('database/3fm_POS_nGrams',paragraph)

	print('360 score:')
	textDifference.main('database/360_POS_nGrams',paragraph)

	print('bright score:')
	textDifference.main('database/bright_POS_nGrams',paragraph)

	print('kidsweek score:')
	textDifference.main('database/kidsweek_POS_nGrams',paragraph)

	print('nos score:')
	textDifference.main('database/nos_POS_nGrams',paragraph)

	print('nrc score:')
	textDifference.main('database/nrc_POS_nGrams',paragraph)

	print('sevendays score:')
	textDifference.main('database/sevendays_POS_nGrams',paragraph)


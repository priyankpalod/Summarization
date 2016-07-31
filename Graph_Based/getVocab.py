def getVocab(text):
	text  = text.strip().replace('-\n','').replace('\n',' ').strip()
	text = set([word.strip('.!?').replace('\'s','') for word in text.lower().split(' ')])
	text = text-set([''])
	terms = {}
	PositionInVector = 0
	for term in text:
		terms[term] = PositionInVector
		PositionInVector += 1
	return terms

# print getVocab('Hello Mrs. N. Mathur, Welcome to our home. Did you have any problems on the way? Comfort yourselves! You must be tired.')
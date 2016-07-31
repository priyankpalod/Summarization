def createVectors(sentences,vocab,idfs):
	vectors = {}
	numTerms = len(vocab)
	numSentence = 0

	# Initialize vectors by tf in the sentence
	for sentence in sentences:
		vectors[numSentence] = [0]*numTerms
		sentence = sentence.strip()
		for term in [word.strip('.!?').replace('\'s','') for word in sentence.lower().split(' ')]:
			# print term
			vectors[numSentence][vocab[term]] += 1
		# print sentence , " : ", vectors[numSentence]
		numSentence += 1
	
	# Multiply by idfs
	for numSentence in vectors:
		vector = vectors[numSentence]
		vectors[numSentence] = [vector[i]*idfs[i] for i in range(numTerms)]
	return vectors
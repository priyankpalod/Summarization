import math
def getIdfs(sentences,vocab):
	idfs = {}
	N = len(sentences)
	for term in vocab:
		termNum = vocab[term]
		count = 0
		for sentence in sentences:
			if term in sentence.lower():
				count+=1
		try:
			idfs[termNum] = math.log(float(N)/count)
			# if idfs[termNum] == 0:
				# print term , "occurs in every sentence!!!"
		except ZeroDivisionError:
			print term + " Occurs nowhere!!!"
	return idfs
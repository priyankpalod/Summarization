def isException(text):
	fullStopExceptions = ['eg.', 'org.', 'al.'] # Other Abbreviations. For eg. 'W.H.O.'
	vowels = ['a','e','i','o','u','y']
	hasVowel = False
	lastWord = text.split(' ')[-1].lower()
	for i in range(len(lastWord)):
		if lastWord[i] in vowels:
			hasVowel = True
			break
	# print lastWord
	if (hasVowel==False) or len(lastWord)<=2 or lastWord in fullStopExceptions:	#len(lastWord)<=2 means only one letter eg. "N." => Abbreviation
		return True
	return False



def parseSentences(text):
	text  = text.strip().replace('-\n','').replace('\n',' ').strip()
	endOfSentenceMarkers = ['.','?', '!']
	INFINITY = len(text) + 1
	sentences = []
	searchFullStopFrom = 0
	while(text!=''):
		# print "Text here =", text
		text = text.strip()
		nextFullStop = searchFullStopFrom + text[searchFullStopFrom:].find('.')
		nextQuestionMark = text.find('?')
		nextExclaimationMark = text.find('!')
		if nextFullStop == -1:
			nextFullStop = INFINITY
		if nextQuestionMark == -1:
			nextQuestionMark = INFINITY
		if nextExclaimationMark == -1:
			nextExclaimationMark = INFINITY
		nextEOS = min(nextFullStop,nextExclaimationMark,nextQuestionMark)
		if nextEOS == INFINITY:
			sentences.append(text)
			break
		if nextEOS==nextFullStop:
			if (nextEOS+1 != len(text) and text[nextEOS+1]!=' ') or isException(text[:nextEOS+1]):
				searchFullStopFrom = nextEOS+1
			else:
				sentences.append(text[:nextEOS+1])
				text = text[nextEOS+1:]
				searchFullStopFrom = 0
		else:
			sentences.append(text[:nextEOS+1])
			text = text[nextEOS+1:]
			searchFullStopFrom = 0
	# print sentences
	return sentences

# testFile = 'Tests/A00-1002.txt'
# with open(testFile,'r') as myTestFile:
# 	text = myTestFile.read()
# for sentences in parseSentences(text):
# 	print sentences

# parseSentences('Hello Mrs. N. Mathur, Welcome to our home. Did you have any problems on the way? Comfort yourselves! You must be tired.')
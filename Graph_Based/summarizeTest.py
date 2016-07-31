from parseSentences import parseSentences
from getVocab import getVocab
from getIDFs import getIdfs
from createVectors import createVectors
from cosineSimilarities import cosineSimilarities
from makeThreshHoldedGraph import makeThreshHoldedGraph
from PageRank import PageRank
import numpy
import copy
import sys
def removeRowAndColoumn(graph,r):
	'''
	removes r-th row and r-th coloumn from the numpy.darray matrix graph
	'''
	newGraph = numpy.zeros((len(graph)-1,len(graph)-1))
	for i in range(len(graph)-1):
		if i==r:
			continue
		for j in range(len(graph[i])-1):
			if j>=r:
				newGraph[i][j] = graph[i][j+1]
	return newGraph


def main(filename,threshold=50):
	with open(filename,'r') as TextToSummarize:
		text = TextToSummarize.read()

	vocab = getVocab(text)
	# print vocab
	sentences = parseSentences(text)
	originalSentences = copy.copy(sentences)
	# for sentence in sentences:
	# 	print sentence
	idfs = getIdfs(sentences,vocab)
	vectors = createVectors(sentences,vocab,idfs)
	similarityMatrix = cosineSimilarities(vectors)
	graph = makeThreshHoldedGraph(similarityMatrix,threshold)
	summarySentences = []
	summary = ''
	# while len(graph!=0):
		# Apply PageRank and pick up the best sentence
		# Re-adjust the graph and other dictionaries
	while len(graph)!=0:
		ranks, degrees = PageRank(graph)
		sentenceNo = ranks.index(max(ranks))
		summarySentences.append(sentences[sentenceNo])
		sentencesTaken = [j for j in range(len(graph[sentenceNo])) if graph[sentenceNo][j]!=0 or sentenceNo==j]
		newSentences = sentences
		j = 0
		for i in range(len(sentences)):
			if i in sentencesTaken:
				graph = removeRowAndColoumn(graph,i)
			else:
				newSentences[j] = newSentences[i]
				j+=1
		sentences = newSentences[:j]

	for sentence in originalSentences:
		if sentence in summarySentences:
			summary+=sentence+'\n'
	summary = summary.strip()
	print summary

filename = sys.argv[1]
try:
	threshold = int(sys.argv[2])
	main(filename,threshold)
except:
	main(filename)
import numpy
def findThreshHold(matrix,percentage):
	vals = []
	for i in range(len(matrix)):
		for j in range(i+1,len(matrix)):
			vals.append(matrix[i][j])
	vals = sorted(set(vals))
	# print vals[-percentage*len(vals)/100]
	return vals[-percentage*len(vals)/100]

def makeThreshHoldedGraph(matrix,threshhold=50):
	threshHold = findThreshHold(matrix,threshhold)	# Gets threshhold as the value for which only param2 % of pairs are more similar 
	graph = numpy.zeros((len(matrix),len(matrix)))
	for i in range(len(graph)):
		for j in range(i+1, len(graph)):
			if(matrix[i][j]>=threshHold):
				graph[i][j] = 1
				graph[j][i] = 1
	# print graph
	return graph
import copy
def makeRowStochiostic(graph1):
	graph = copy.copy(graph1)
	i = 0
	degrees = []
	for row in graph:
		sum_row = 0
		for val in row:
			sum_row+=val
		# print sum_row
		degrees.append(sum_row)
		if sum_row!=0:
			for j in range(len(graph[i])):
				graph[i][j] = float(graph[i][j])/sum_row
				graph[j][i] = graph[i][j]
		i+=1
	return graph,degrees

def PageRank(graph1):
	'''
	This page rank is implemented for undirected graph, therefore there is no need for the 'beta' component as there isn't any
	zero propogation in undirected graph
	'''
	graph, degrees = makeRowStochiostic(graph1)
	# print graph
	# print degrees
	# exit(0)
	ConvergenceThreshhold = 0.001
	sqdiff = 1
	ranks = [1]*len(graph)
	newRanks = [1]*len(graph)
	while sqdiff>ConvergenceThreshhold:
		for i in range(len(graph)):
			x = 0
			for j in range(len(graph[i])):
				if graph[i][j]!=0:
					if degrees[j]==0:
						print 'Whaaaat!!!?? :/ '#, graph[i][j]
						print graph
						print degrees
						print 'i=',i,'j=',j
						exit(0)
					else:
						x += graph[i][j]*ranks[j]/degrees[j]
			newRanks[i] = x

		sqdiff = 0
		for i in range(len(graph)):
			sqdiff += (newRanks[i]-ranks[i])**2

		ranks = newRanks

	return ranks,degrees

import numpy
import math

def cosine_simlarity(vector1,vector2):
	sumx = 0
	norm1 = 0.0
	norm2 = 0.0

	for element1,element2 in zip(vector1,vector2):
	    sumx = sumx + element1*element2
	    norm1 = norm1 + element1 * element1
	    norm2 = norm2 + element2 * element2     


	norm1 = math.sqrt(norm1)
	norm2 = math.sqrt(norm2)

	if norm1==0 or norm2==0:
		ans = 0
	else:
		ans = sumx/(norm1*norm2)

	return ans

def cosineSimilarities(vectors):
	matrix = numpy.zeros((len(vectors),len(vectors)))
	for vector1Num in vectors:
		for vector2Num in vectors:
			if vector1Num>=vector2Num:
				matrix[vector1Num][vector2Num] = matrix[vector2Num][vector1Num]
			else:
				matrix[vector1Num][vector2Num] = cosine_simlarity(vectors[vector1Num], vectors[vector2Num])
	return matrix
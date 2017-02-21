# coding: utf-8

GROUP = (SETOSA, VERSICOLOR, VIRGINICA) = 1, 2, 3	# defining constants
dataTrainning, dataTotal = 105, 150					# dataTotal is equals to number of lines in the file
k = 3												# K is the number of classes

database 	= []									# Will contains the data training
tests		= []									# Will contains the tests
correct 	= 0										# Number of correct answers	
idx 		= 0										# Index of tests

file = open("database", 'r')						# Database file

def euclideanDistance(x, y):
	return ((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2 + (x[3]-y[3])**2) **0.5

def sortSample(candidate):
	global database, dataTrainning, k
	classes 	= []
	distances	= []

	for element in GROUP:
		classes.append([0, element])

	for individual in database:
		dataCandidate = euclideanDistance(candidate, individual)
		distances.append((dataCandidate, individual[-1]))

	distances.sort()

	for i in xrange(k):
		classes[ int(distances[i][1])-1 ][0] += 1

	classes.sort()
	return classes[-1][1]							# Returns the element of greater frequency

for i in xrange(dataTrainning):						# Training the algorithm
	line = map(float, file.readline().split())
	database.append(line)

for i in xrange(dataTrainning, dataTotal):			# Add the test cases
	line = map(float, file.readline().split())
	tests.append(line)

for current in tests:								# Trying the algorithm
	if sortSample(current) == tests[idx][-1]:
		correct += 1
	idx += 1

print 'Number of correct answers: %d/%d' %(correct, dataTotal-dataTrainning)
# Calculate accuracy percentage between two lists 
def accuracy_metrics(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
			return correct /float(len(actual)) * 100.0

# Test accuracy 
actual = [0,0,0,0,0,1,1,1,1,1,]
predicted = [0,1,0,0,0,1,0,1,1,1]

accuracy = accuracy_metrics(actual, predicted)
print(accuracy)


# calculate a confusion matrix
def confusion_matrix(actual, preedicted):
	unique = set(actual)
	matrix = [list() for x in range (len(unique))]
	for i in range(len(unique)):
		matrix[i] = [0 for x in range(len(unique))]
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value]=i
	for i in range(len(actual)):
		x=lookup[actual[i]]
		y=lookup[predicted[i]]
		matrix [x][y] += 1
	return unique,matrix 

# Test confusion matrix with integers
actual = [0,0,0,0,0,1,1,1,1,1]
predicted = [0,1,1,0,0,1,0,1,1,1]
unique, matrix = confusion_matrix(actual, predicted)
print(unique)
print(matrix)

# pretty print a confusion matrix 
def print_confusion_matrix(unique, matrix):
	print('(P' + ''.join(str(x) for x in unique))
	print('(A)----')
	for i, x in enumerate(unique):
		print("%s | %s"%(x, ''.join(str(x) for x in matrix[i])))

# Test confusion matrix with integers 
actual =[0,0,0,0,1,1,1,1,1]
predicted = [0,1,1,0,0,1,0,1,1,1]
unique,matrix = confusion_matrix(actual, predicted)
print_confusion_matrix(unique,matrix)

# Calculate mean absolute error
def mae_metric(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        sum_error += abs(predicted[i]-actual[i])
    return sum_error / float(len(actual))


# Test MSE 
actual = [0.1, 0.2, 0.3, 0.4, 0.5]
predicted = [0.11, 0.19, 0.29, 0.41, 0.5]

mae = mae_metric(actual, predicted)
print(mae)	



# Example of Calculating the Root Mean Square Error 
from math import sqrt 

# Calculate root, mean squared error
def rmse_metric(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error=predicted[i] - actual[i]
        sum_error += (prediction_error ** 2)
    mean_error = sum_error / float(len(actual))
    return sqrt(mean_error)

# Test RMSE 
actual = [0.1, 0.2, 0.3, 0.4, 0.5]
predicted = [0.11, 0.19, 0.29, 0.41, 0.5]
rmse = rmse_metric(actual, predicted)
print(rmse)

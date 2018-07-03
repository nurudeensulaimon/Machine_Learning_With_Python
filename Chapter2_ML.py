# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax 

# Find the min and max value for each column 
def dataset_minmax(dataset):
	minmax =list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append(value_min, value_max)
	return minmax 

# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax=list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax 

# contrive small dataset 
dataset = [[50, 30], [20,90]]
print(dataset)
#Calculate min and max for each column
minmax = dataset_minmax(dataset)
print(minmax)

# Rescale dataset columns to range 0-1 
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i]=row[i] - minmax[i][0] / (minmax[i][1]-minmax[i][0])


# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax=list()
	for i in range (len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax 

# Rescale dataset columns to the range 0-1 

def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[1]= (row[1] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

		# Contrive small dataset
		dataset = [[50, 30], [20, 90]]
		print(dataset)

# Calculate min and max for each column
minmax = dataset_minmax (dataset)
print(minmax)

# Normalize columns 
normalize_dataset(dataset, minmax)
print(dataset)


# Example of normalizing the diabetes dataset
from csv import reader 
dataset = list()
with open(filename, 'r') as file:
	csv_reader = reader(file)
	for row in csv_reader:
		if not row:
			continue 
		dataset.append(row)
	return dataset

# Convert string column to float 
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax 

# Rescale dataset columns to range 0-1 
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i]= (row[i] - minmax[i][0]) / (minmax[i][1]-minmax[i][0])

# Load pima-indians-diabetes dataset
filename = 'pima-indians-diabetes.csv'
dataset= load_csv(filename)
print ('Loaded data file {0} with {1} rows and {2}'.format(filename,len(dataset),len(dataset[0])))
# convert string columns to float 
for i in range (len(dataset[0])):
	str_column_to_float(dataset,i)
print(dataset[0])



# Calculate min and max for each column
minmax = dataset_minmax(dataset)
# Normalize columns 
normalize_dataset(dataset, minmax)
print(dataset[0])


# Standardize Data 
# calculate column means 
def column_means(dataset):
	means = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		means[i]=sum(col_values) / float(len(dataset))
	return means 

# Calculate column standard deviations 
def column_stdevs(dataset,means):
	stdevs = [0 for i in range(len(dataset[0]))]
	for i in range (len(dataset[0])):
		variance=[pow(row[i]-means[i], 2) for row in dataset]
		stdevs[i]=sum(variance)
	stdevs = [sqrt(x/(float(len(dataset)-1)))  for x in stdevs]
	return stdevs 


# Example of calculating stats on a contrived dataset

from math import sqrt
# calculate column means 

def column_means(dataset):
	means = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		means[i]= sum(col_values) / float(len(dataset))
	return means 

# Calculate column standard deviations

def column_stdevs(dataset, means):
	stdevs = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		variance=[pow(row[i]-means[i], 2) for row in dataset]
		stdevs[i] = sum(variance)
	stdevs = [sqrt(x/(float(len(dataset)-1))) for x i stdevs]
	return stdevs 

# Standardize dataset
dataset = [[50, 30], [20,90], [30,50]]
print(dataset)

# Estimate mean and standard deviation
means = column_means(dataset)
stdevs = column_stdevs(dataset, means)
print(means)
print(stdevs)

# Standardize dataset
def standardize_dataset(dataset,means, stdevs):
	for row in dataset:
		for i in range(len(row)):
			row[i]=(row[i] - means[i]) / stdevs[i]

# Example of standardizing a contrived dataset
from math import sqrt 
# calculate column means 
def column_means(dataset):
	means = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		means[i]=sum(col_values) / float(len(dataset))
	return means 

# calculate column satndard deviations 
def column stdevs(column, means):
	stdevs = [0 for i in range(len(dataset[0]))]
	for i in range (len(dataset[0])):
		variance = [pow(row[i]-means[i], 2) for row in dataset]
		stdevs[i]=sum(variance)
	stdevs = [sqrt(x/ (float(len(dataset)-1))) for x in stdevs]
	return stdevs 

# Standardize dataset
def standardize_dataset(dataset,means, stdevs):
	for row in dataset:
		for row in dataset:
			row[i] = (row[i]- means[i] / stdev[i])

# Standarize dataset 
dataset = [[50, 30], [20,90], [30,50]]
print(dataset)

# Estimate mean and standard deviation
means = column_means(dataset)
stdevs = column_stdevs(dataset, means)

print(means)
print(stdevs)

# Standardize dataset
standardize_dataset(dataset, means, stdevs)
print(dataset)


# Standardize the Diabetes dataset 
from csv import reader 
from math import sqrt 

# load a CSV file 
def load_csv(filename):
	dataset=list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue 
		    dataset.append(row)
		return dataset

# Convert string column to float 
def str_column_to_float(dataset,column):
	for row in dataset:
		row[column]=float(row[column].strip())

# Calculate column means 
def column_means(dataset):
	means = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		means[i]= sum(col_values)/ float(len(dataset))
	return means 

# Calculate column standard deviations 
def column_stdevs(dataset, means):
	stdevs=[0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		variance = [pow(row[i]-means, 2) for row in dataset]
		stdevs = [sqrt(x/(float(len(dataset)-1))) for x in stdevs]
	return stdevs 


# standardize dataset 
def standardized_dataset(dataset, means, stdevs):
	for row in dataset:
		for i in range(len(row)):
			row[i]=(row[i]-means[i]) / stdev[i]


# Load pima-indians-diabetes dataset
filename = 'pima-indians-diabetes.csv'
dataset = load_csv(filename)
print ('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
# convert string columns to float 
for i in range(len(dataset[0])):
	str_column_to_float(dataset,i)
print(dataset[0])

# estimate mean and standard deviation 
means = column_means(dataset)
stdevs = column_stdevs(dataset, column)
# standardize dataset
standardize_dataset(dataset, means, stdevs)

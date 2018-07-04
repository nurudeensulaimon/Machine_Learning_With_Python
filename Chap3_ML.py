# Chapter 3
# Algorithm Evaluation Methods
# How to implement a train and test split of your data 
# How to implement a k-fold cross-validation split of your data.

# Description
# The goal of resampling methods is to make the best use of your 
# training data in order to accurately estimate the performance of a 
# model on new unseen data.

# Example of Splitting a Contrived dataset into Train and Test 
from random import seed
from random import randrange 

# Split a dataset into a train and test set
def train_test_split(dataset, split=0.60)

def train_test_split(dataset, split=0.60):
	train=list()
	train_size=split * len(dataset)
	dataset_copy = list(dataset)
	while len(train) < train_size:
		index=randrange(len(dataset_copy))
		train.append(dataset_copy.pop(index))
	return train, dataset_copy

# test train/test split 
seed(1)
dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
train, test=train_test_split(dataset)
print(train)
print(test)

# split a dataset into K folds

def cross_validation_split(dataset, fold=3):
	dataset_split=list()
	dataset_copy=list(dataset)
	fold_size=int(len(dataset) / folds)
    for i in range (folds):
    	fold=list()
    	while len(fold) < fold_size:
    		index=randrange(len(dataset_copy))
    		fold.append(dataset_copy.pop(index))
    		dataset_split.append(fold)
    return dataset_split

# test cross validation split 
seed(1)
dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
folds = cross_validation_split(dataset,4)
print(folds)

# Extensions 
# Repeated Train and Test 
# LOOCV or Leave one Out Cross Validation. This is a form of k-fold cross
# validation where the value of k is fixed at 1 

# Stratification In classification problems, this is where the balance of class values in
# each group is forced to match the original dataset.

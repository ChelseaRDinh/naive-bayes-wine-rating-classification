import importlib
import sklearn
import numpy as np
import pandas as pd
#GaussianNB makes most sense because it is rule-based.
#We will use GaussianNB with numeric attributes.
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
#Calculate accuracy score of our classifier
from sklearn.metrics import accuracy_score
#Split data in to train and test sets.
from sklearn.model_selection import train_test_split
#Read train and test data from csv files
import csv

#Variables for our data set:
#region
#designation
#country
#province
#winery
#variety
#price(?) --> If we want to deal with numeric attributes.

def categorizeData():
    columns = pd.read_csv('winemag-data_first150k.csv')
    attributes = []
    class_vals = []

    i = 0
    for c in columns:
        if i != 0:
            attributes.append(c)
        i = i+1
    
    reader = csv.reader(open('winemag-data_first150k.csv', newline=''))
    #create list of instances that are strings, where each field is separated as a unique object
    instances = []
    i = 0
    for row in reader:
        if i != 0:
            #remove first val of row, which is just the index of the instance in the csv file.
            instances.append(row[1:])
            #Make a list of class values, in our case, wine rating points for each wine instance.
            class_vals.append(int(row[4]))
        i = i+1
    return attributes, instances, class_vals

def main():
    #Testing sklearn method functionality.
    classifier = GaussianNB()
    attributes, instances, class_vals = categorizeData()
    #print('Attributes: '+str(attributes)+'\n\n')
    #Test print out a few of the rows just to make sure they're formatted correctly.
    #for i in range(10):
        #print('Row '+str(i)+': '+str(instances[i])+'\n')
    #for i in range(10):
        #print(class_vals[i])
#call main method
main()
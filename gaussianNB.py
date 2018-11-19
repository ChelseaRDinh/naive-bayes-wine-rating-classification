import importlib
import sklearn
import numpy as np
import pandas as pd
#GaussianNB makes most sense because it is rule-based.
from sklearn.naive_bayes import GaussianNB
#Calculate accuracy score of our classifier
from sklearn.metrics import accuracy_score
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
    return 0

def main():
    #Testing sklearn method functionality.
    classifier = GaussianNB()
    print("Hello world.")

main()
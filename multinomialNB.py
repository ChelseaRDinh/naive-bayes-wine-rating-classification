import importlib
import sklearn
import numpy as np
import pandas as pd
import re
#Classifying wine reviews using multinomialNB --> text classification
from sklearn.naive_bayes import MultinomialNB
#Calculate accuracy score of our classifier
from sklearn.metrics import accuracy_score
#Split data in to train and test sets.
from sklearn.model_selection import train_test_split
#Read train and test data from csv files
import csv

#We will be classifying the instances based on their description to the appropriate class value (wine points)

def parseData():
    class_vals = []
    
    reader = csv.reader(open('winemag-data_first150k.csv', newline=''))
    #create list of instances that are strings, where each field is separated as a unique object
    text_instances = []
    i = 0
    for row in reader:
        if i != 0:
            #split row in to terms
            #Use regex to split row based on spaces, commas, and periods.
            sentence = re.findall(r"[\w']+", row[2])
            text_instances.append(sentence)
            #Make a list of class values, in our case, wine rating points for each wine instance.
            class_vals.append(int(row[4]))
        i = i+1
    return text_instances, class_vals

def main():
    #instantiate multinomial naive bayes classifier
    classifier = MultinomialNB()
    text_instances, class_vals = parseData()
    #Test print out a few of the rows just to make sure they're formatted correctly.
    #for i in range(10):
       #print('Row '+str(i)+': '+str(text_instances[i])+'\n')
    #for i in range(10):
        #print(class_vals[i])

main()
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
    labels = []
    reader = csv.reader(open('winemag-data_first150k.csv', newline=''))
    #create list of instances that are strings, where each field is separated as a unique object
    text_instances = []
    train_instances = []
    train_labels = []
    i = 0
    for row in reader:
        if i != 0:
            #testing with only 100 instances for now; the data in the file requires a lot of computation.
            if i <= 100:
                #split row in to terms
                #Use regex to split row based on spaces, commas, and periods.
                sentence = re.findall(r"[\w']+", row[2])
                text_instances.append(sentence)
                #Make a list of class values, in our case, wine rating points for each wine instance.
                labels.append(int(row[4]))
            elif i > 100 and i <=200:
                sentence = re.findall(r"[\w']+", row[2])
                train_instances.append(sentence)
                train_labels.append(int(row[4]))
            else:
                break
        i = i+1
    return text_instances, labels

def createVocabAndClasses(text_instances, labels):
    V = []
    for sentence in text_instances:
        for word in sentence:
            if V.count(word) == 0:
                V.append(word)
    C = []
    for val in labels:
        if C.count(val) == 0:
            C.append(val)

    return V, C

def countTermsInDocs(text_instances, V):
    term_occurrences = np.zeros([len(V)])
    for sentence in text_instances:
        for word in sentence:
            if V.count(word) != 0:
                term_occurrences[V.index(word)] = term_occurrences[V.index(word)]+1
    return term_occurrences

def createDictionary(text_instances, labels):
    D = []
    for i in range(len(text_instances)):
        obj = {'class': int(labels[i]), 'doc': text_instances[i]}
        D.append(obj)
    return D

def main():
    #instantiate multinomial naive bayes classifier
    classifier = MultinomialNB()
    text_instances, labels = parseData()
    V, C = createVocabAndClasses(text_instances, labels)
    term_occurrences = countTermsInDocs(text_instances, V)
    D = createDictionary(text_instances, labels)
    #for d in D:
        #print(str(d)+'\n')
    #print amount of occurrences per term
    #for term_occurrence in term_occurrences:
        #print(term_occurrence)
    #for doc in text_instances:
        #print('Row: '+str(text_instances.index(doc))+str(doc)+'\n')

main()
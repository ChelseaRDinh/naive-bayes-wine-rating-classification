import importlib
import sklearn
import numpy as np
import pandas as pd
#GaussianNB makes most sense because it is rule-based.
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

#Variables for our data set:
#region
#designation
#country
#province
#winery
#variety
#price(?) --> If we want to deal with numeric attributes.

def main():
    #Testing sklearn method functionality.
    classifier = GaussianNB()
    print("Hello world.")

main()
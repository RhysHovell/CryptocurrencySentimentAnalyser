import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.classify.scikitlearn import SklearnClassifier

from imblearn.over_sampling import SMOTE

import pickle
import seaborn as s
import pandas as p
import numpy as np
import matplotlib.pyplot as plot

import math
import random
from collections import Counter

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

precision = 1

tokenizer = RegexpTokenizer(r'\w+')

stopWords = set(stopwords.words('english'))

allPositiveWords = []
allNegativeWords = []

count = 0

with open("Data/positiveNews.txt", "r", encoding='utf-8',
          errors='ignore') as positive:
    for line in positive.readlines():
        count += 1
        word = tokenizer.tokenize(line)
        for w in word:
            if w.lower() not in stopWords:
                allPositiveWords.append(w.lower())

with open("Data/negativeNews.txt", "r", encoding='utf-8',
          errors='ignore') as negative:
    for i, line in enumerate(negative):
        if i == count:
            break
        word = tokenizer.tokenize(line)
        for w in word:
            if w.lower() not in stopWords:
                allNegativeWords.append(w.lower())

allWords = nltk.FreqDist(allPositiveWords+allNegativeWords)
feat = [x[0] for x in allWords.most_common(1500)]


print(allNegativeWords[:10])
print(allPositiveWords[:10])


def f_creation(wList):
    features = {}
    for w in feat:
        features[w] = w in wList
    return features


f_sets = []
with open("Data/positiveNews.txt", "r", encoding='utf-8',
          errors='ignore') as positive:
    for line in positive.readlines():
        temp = []
        word = tokenizer.tokenize(line)
        for w in word:
            if w.lower() not in stopWords:
                temp.append(w.lower())
        f_sets.append((f_creation(temp), 1))

with open("Data/negativeNews.txt", "r", encoding='utf-8',
          errors='ignore') as negative:
    for i, line in enumerate(negative):
        temp = []
        if i == count:
            break
        word = tokenizer.tokenize(line)
        for w in word:
            if w.lower() not in stopWords:
                temp.append(w.lower())
        f_sets.append((f_creation(temp), -1))

from sklearn.model_selection import ShuffleSplit

random.shuffle(f_sets)
runs = []
num_folds = 10
ss = ShuffleSplit(n_splits=10, test_size=0.2)

subsetSize = math.ceil(len(f_sets) / num_folds)

'''
for i in range(num_folds):
    classifierList = []
    trainSet = (f_sets[(i + 1) * subsetSize:]
                    + f_sets[:i * subsetSize])
    testSet = f_sets[i * subsetSize:(i + 1) * subsetSize]

    nb = nltk.NaiveBayesClassifier.train(trainSet)

    classifierList.append(nb)
    runs.append((nltk.classify.accuracy(nb, testSet)) * 100)
    print("Naive Bayes Accuracy:", round(runs[-1], precision))


'''

for i in range(num_folds):
    classifierList= []
    trainSet = (f_sets[(i + 1) * subsetSize:] + f_sets[:i * subsetSize])
    testSet = f_sets[i * subsetSize:(i + 1) * subsetSize]

    lr = SklearnClassifier(LogisticRegression())
    lr.train(trainSet)

    runs.append((nltk.classify.accuracy(lr, testSet)) * 100)
    print("Logistic Regression Accuracy:", round(runs[-1], precision))


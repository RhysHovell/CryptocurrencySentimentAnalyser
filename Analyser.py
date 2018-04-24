import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.classify.scikitlearn import SklearnClassifier

import seaborn as s
import pandas as p
import numpy as np
import matplotlib.pyplot as plot

import math
import random
from collections import Counter


def analyse():
    tokenizer = RegexpTokenizer(r'\w+')

    sw = set(stopwords.words('english'))

    allPositiveWords = []
    allNegativeWords = []

    with open("Data/positiveNews.txt", "r", encoding='utf-8',
              errors='ignore') as positive:
            for line in positive.readlines():
                word = tokenizer.tokenize(line)
                for w in word:
                    if w.lower() not in sw:
                        allPositiveWords.append(w.lower())

    cp = Counter(allPositiveWords)
    positiveResult = nltk.FreqDist(allPositiveWords)

    mostCommonPos = allPositiveWords[:10]
    print(mostCommonPos)
    with open("Data/negativeNews.txt", "r", encoding='utf-8',
              errors='ignore') as negative:
            for line in negative.readlines():
                word = tokenizer.tokenize(line)
                for w in word:
                    if w.lower() not in sw:
                        allNegativeWords.append(w.lower())

    negativeResult = nltk.FreqDist(allNegativeWords)

    mostCommonNeg = allNegativeWords[:10]
    print(mostCommonNeg)
    plot.style.use('bmh')

    y = [x[1] for x in positiveResult.most_common(len(allPositiveWords))]




    plot.xlabel("Words")
    plot.ylabel("Number of Mentions")
    plot.title("Word Distribution - Positive")
    plot.plot(y)
    plot.savefig("static/positiveDist.png")
    plot.show()

    y = [x[1] for x in negativeResult.most_common(len(allNegativeWords))]

    plot.xlabel("Words")
    plot.ylabel("Number of Mentions")
    plot.title("Word Distribution - Negative")
    plot.plot(y)
    plot.savefig("static/negativeDist.png")
    plot.show()


    return (mostCommonPos, mostCommonNeg)

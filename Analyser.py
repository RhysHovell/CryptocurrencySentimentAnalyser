import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import math

example = "This is an example sentence!, However, it "\
            "is a very informative one,"

tokenizer = RegexpTokenizer(r'\w+')

stop_words = set(stopwords.words('english'))

all_positive_words = []

with open("positiveNews.text", "r", encoding='utf-8',
          errors='ignore') as positive:
        for line in positive.readlines():
            word = tokenizer.tokenize(line)
            for w in word:
                if w.lower() not in stop_words:
                    all_positive_words.append(w.lower())

positive_result = nltk.FreqDist(all_positive_words)


all_negative_words = []

with open("negativeNews.txt", "r", encoding='utf-8',
          errors='ignore') as negative:
        for line in negative.readlines():
            word = tokenizer.tokenize(line)
            for w in word:
                if w.lower() not in stop_words:
                    all_negative_words.append(w.lower())

negative_result = nltk.FreqDist(all_negative_words)


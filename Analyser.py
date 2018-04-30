import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


import matplotlib.pyplot as plot




tokenizer = RegexpTokenizer(r'\w+')

sw = set(stopwords.words('english'))

def analyse():
    allPositiveWords = []
    allNegativeWords = []


    with open("Data/positiveNews.txt", "r", encoding='utf-8',
              errors='ignore') as positive:
            for line in positive.readlines():
                word = tokenizer.tokenize(line)
                for w in word:
                    if w.lower() not in sw:
                        allPositiveWords.append(w.lower())

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

    y = [x[1] for x in positiveResult.most_common()]

    plot.plot(y)
    plot.xlabel("Words")
    plot.ylabel("Number of Mentions")
    plot.title("Word Distribution - Positive")
    plot.savefig("static/positiveDist.png")
    plot.close()

    y = [x[1] for x in negativeResult.most_common()]

    plot.plot(y)
    plot.xlabel("Words")
    plot.ylabel("Number of Mentions")
    plot.title("Word Distribution - Negative")
    plot.savefig("static/negativeDist.png")
    plot.close()

    return mostCommonPos, mostCommonNeg
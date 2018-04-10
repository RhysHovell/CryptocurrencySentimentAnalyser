import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plot
import math

example = "This is an example sentence!, However, it "\
            "is a very informative one,"

tokenizer = RegexpTokenizer(r'\w+')

stopWords = set(stopwords.words('english'))

allPositiveWords = []

with open("Data/positiveNews.txt", "r", encoding='utf-8',
          errors='ignore') as positive:
        for line in positive.readlines():
            word = tokenizer.tokenize(line)
            for w in word:
                if w.lower() not in stopWords:
                    allPositiveWords.append(w.lower())

positiveResult = nltk.FreqDist(allPositiveWords)
print(positiveResult.most_common(12))

allNegativeWords = []

with open("Data/negativeNews.txt", "r", encoding='utf-8',
          errors='ignore') as negative:
        for line in negative.readlines():
            word = tokenizer.tokenize(line)
            for w in word:
                if w.lower() not in stopWords:
                    allNegativeWords.append(w.lower())

negativeResult = nltk.FreqDist(allNegativeWords)
print(negativeResult.most_common(12))

plot.style.use('ggplot')

y = [x[1] for x in positiveResult.most_common(len(allPositiveWords))]
yResult = []

for i, k, z, t in zip(y[0::4], y[1::4], y[2::4], y[3::4]):
    yResult.append(math.log(i+k+z+t))
x = [math.log(i+1) for i in range(len(yResult))]

plot.xlabel("Words")
plot.ylabel("Frequency")
plot.title("Word Distribution - Positive")
plot.plot(x, yResult)
plot.savefig("positiveDist.png")
plot.show()


y = [x[1] for x in negativeResult.most_common(len(allNegativeWords))]
yResult = []
for i, k, z in zip(y[0::3], y[1::3], y[2::3]):
    yResult.append(math.log(i + k + z + t))
    if i+k+z == 0:
        break
        yResult.append(math.log(i+k+z))
x = [math.log(i+1) for i in range(len(yResult))]

plot.xlabel("Words")
plot.ylabel("Frequency")
plot.title("Word Distribution - Negative")
plot.plot(x, yResult)
plot.savefig("templates/negativeDist.png")
plot.show()





from cycler import cycler
import matplotlib.pyplot as plot
import numpy as np
from Headlines import headlines

def chart():
    positive, negative = headlines()

    numPos = len(positive)
    numNeg = len(negative)

    print(numPos)
    print(numNeg)

    if numPos > numNeg:
        numNeu = (numPos - numNeg)
    else:
        numNeu = (numNeg - numPos)

    y = [numNeu, numNeg, numPos]
    x = [1, 2, 3]


    plot.style.use('bmh')

    index = np.arange(len(x))
    width = 0.5
    figure, axis = plot.subplots()
    axis.bar(index+0.3, y, width, color="orange")
    axis.set_xticks(index+0.05+width/2)
    axis.set_xticklabels(['Neutral', 'Negative', 'Positive'])
    plot.title("Sentiment Distribution")
    plot.ylabel("No Of Posts")
    plot.savefig("static/sentiment_dist.png")
    plot.show()

from cycler import cycler
import matplotlib.pyplot as plot
import numpy as np
from Headlines import headlines





def chart():
    positive, negative = headlines()
    numPos = positive.count()
    numNeg = negative.count()
    y = [448/982*100, numNeg, numPos]
    x = [1, 2, 3]

    plot.style.use('bmh')

    index = np.arange(len(x))
    width = 0.5
    figure, axis = plot.subplots()
    axis.bar(index+0.3, y, width, color="orange")
    axis.set_xticks(index+0.05+width/2)
    axis.set_xticklabels(['Neutral', 'Negative', 'Positive'])
    plot.title("Sentiment Distribution")
    plot.ylabel("Percentage %")
    plot.savefig("static/sentiment_dist.png")
    plot.show()

import matplotlib.pyplot as plot
import numpy as np

y = [448/982*100, 307/982*100, 227/982*100]
x = [1, 2, 3]

plot.style.use('ggplot')

index = np.arange(len(x))
width = 0.5
figure, axis = plot.subplots()
axis.bar(index+0.1, y, width, color='green')
axis.set_xticks(index+0.0+width/2)
axis.set_xticklabels(['Neutral', 'Negative', 'Positive'])
axis.legend("X")
plot.title("Sentiment Distribution")
plot.xlabel("Sentiment")
plot.ylabel("%")
plot.savefig("templates/sentiment_dist.png")
plot.show()

from flask import Flask, render_template

import matplotlib.pyplot as plot
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():

    return render_template("home.html")


y = [448/982*100, 307/982*100, 227/982*100]
x = [1, 2, 3]

plot.style.use('ggplot')

index = np.arange(len(x))
width = 0.5
figure, axis = plot.subplots()
axis.bar(index+0.1, y, width, color='green')
axis.set_xticks(index+0.0+width/2)
axis.set_xticklabels(['Neutral', 'Negative', 'Positive'])
axis.legend()
plot.title("Sentiment Distribution")
plot.xlabel("Sentiment")
plot.ylabel("%")
plot.show()


if __name__ == '__main__':
    app.run(debug=True)





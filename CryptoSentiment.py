from flask import Flask, render_template, url_for
from Headlines import headlines
from Analyser import analyse
from Chart import chart

app = Flask(__name__, static_url_path='/static')


mostCommonPos, mostCommonNeg = analyse()


@app.route('/')
def home():

    negList = str(mostCommonNeg).replace('[', '').replace(']', '').replace(',', '')
    posList = str(mostCommonPos).replace('[', '').replace(']', '').replace(',', '')

    negList.join(negList)
    posList.join(posList)
    return render_template('home.html', negList=negList, posList=posList)


@app.route('/headline')
def headline():
    headlines()
    analyse()
    chart()
    return home()


if __name__ == '__main__':
    app.run()





from flask import Flask, render_template, request
from Headlines import headlines
from Analyser import analyse
from Chart import chart

app = Flask(__name__, static_url_path='/static')


mostCommonPos, mostCommonNeg = analyse()


@app.route('/')
def home():

    negList = str(mostCommonNeg).replace('[', '').replace(']', '').replace(',', '')
    posList = str(mostCommonPos).replace('[', '').replace(']', '').replace(',', '')

    return render_template('home.html', negList=negList, posList=posList)


@app.route('/home.html')
def other():

    negList = str(mostCommonNeg).replace('[', '').replace(']', '').replace(',', '')
    posList = str(mostCommonPos).replace('[', '').replace(']', '').replace(',', '')

    return render_template('home.html', negList=negList, posList=posList)


@app.route('/headline')
def main():
    headlinesS()
    analyse()
    chartS()
    return home()


def headlinesS():
    headlines()
    return render_template('home.html', status='Headlines Retrieved')


def chartS():
    chart()
    return render_template('home.html', status='Finished')

@app.route('/word.html')
def word():
    negList = str(mostCommonNeg).replace('[', '').replace(']', '').replace(',', '')
    posList = str(mostCommonPos).replace('[', '').replace(']', '').replace(',', '')

    return render_template('word.html', negList=negList, posList=posList)


if __name__ == '__main__':
    app.run()





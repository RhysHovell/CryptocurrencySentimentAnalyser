from flask import Flask, render_template, url_for
app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('home.html')


if __name__ == '__main__':
    app.run()





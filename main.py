import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    some_text = 'this is some text'
    now = str(datetime.datetime.now())

    seznam_mest = ['Ljubljana', 'Maribor', 'Celje', 'Koper']

    return render_template("index.html",
                           input_text=some_text,
                           todays_date=now,
                           mesta=seznam_mest
                           )


@app.route('/o-meni')
def about_me():
    return render_template("about.html")


@app.route('/o-meni/kontakt')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(use_reloader=True)


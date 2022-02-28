from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/o-meni')
def about_me():
    return render_template("about.html")


@app.route('/o-meni/kontakt')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(use_reloader=True)


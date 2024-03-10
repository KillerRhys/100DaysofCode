""" Name Card?
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.03.10(1308) """


# Imports.
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

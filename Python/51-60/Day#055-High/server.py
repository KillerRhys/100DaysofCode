""" High / Low Site
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.03.09(1018) """

# Imports.
from flask import Flask
import random

# Main file identifier.
app = Flask(__name__)

# Constants.
global NUMBER_TO_GUESS
NUMBER_TO_GUESS= random.randint(0, 9)
COLORS = ['red', 'orange', 'green', 'blue', 'indigo', 'violet']


# Decorators
def make_bold(function):
    def wrapper():
        text = function()
        return f'<b>{text}</b>'

    wrapper.__name__ = function.__name__
    return wrapper


def make_emphasis(function):
    def wrapper():
        text = function()
        return f'<em>{text}</em>'

    wrapper.__name__ = function.__name__
    return wrapper


def make_underline(function):
    def wrapper():
        text = function()
        return f'<u>{text}</u>'

    wrapper.__name__ = function.__name__
    return wrapper


@app.route('/')
@make_bold
def hello_world():
    return ("<center><h1>Let's play a game!<h1></center>"
            "<center><h2>Guess the number between 0-9</h2></center>" 
            "<center><img src='https://media4.giphy.com/media/dByxF08foiugLFd1Q7/giphy.webp?cid=790b7611xgm7h86aiw6"
            "puadf3rxtv5djxuzyknq7gqzw028f&ep=v1_gifs_search&rid=giphy.webp&ct=g'></center> ")


@app.route('/bye')
@make_bold
@make_underline
@make_emphasis
def bye():
    return "Bye!"


@app.route('/replay')
def replay():
    global NUMBER_TO_GUESS
    NUMBER_TO_GUESS= random.randint(0, 9)
    return (f"<center><font color={random.choice(COLORS)}><h1>Here we go again!!</h1></font></center>"
            f"<center><h2>I've got a new number!</h2></center>"
            f"<center><img src='https://media4.giphy.com/media/dZEoQE2qlzwx3IP98G/200.webp?cid=790b7611cd0ascmeb7rsjk"
            f"r4tsvmd3x7em64fb2dyyi9qexh&ep=v1_gifs_search&rid=200.webp&ct=g'></center>")


@app.route('/<int:guess>')
# @random_color
def guess_number(guess):
    if guess > NUMBER_TO_GUESS:
        return (f"<center><font color={random.choice(COLORS)}><h1>Too High!</h1></font></center>"
                f"<center><h2>You guessed: {guess}...</h2></center>"
                f"<center><img src='https://media3.giphy.com/media/s1MX7LfOn5nhTyb0dy/giphy.webp?cid=790b7611gon76m77"
                f"1n8rxxfyamwburek54nhipircewc5cs2&ep=v1_gifs_search&rid=giphy.webp&ct=g'></center>")

    elif guess < NUMBER_TO_GUESS:
        return (f"<center><font color={random.choice(COLORS)}><h1>Too Low!</h1></font></center>"
         f"<center><h2>You guessed: {guess}...</h2></center>"
         f"<center><img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNG5oMzB5MHhzZTE5ejd3eWlpMzB1bWt4MXJia29"
                f"6cWd1cWs0anpvYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7TKHVU0xsgGDCyPu/200.webp'></center>")

    elif guess == NUMBER_TO_GUESS:
        return (f"<center><font color={random.choice(COLORS)}><h1>You got it!!!</h1></font></center>"
                f"<center><h2>The number was: {guess}!</h2></center>"
                f"<center><img src='https://media1.giphy.com/media/OsbjNV7eOpYvDv4VN0/giphy.webp?cid=790b7611j3onpujyh"
                f"itsn7gh2pf2bndspnjhp0xp9kz3y0rg&ep=v1_gifs_search&rid=giphy.webp&ct=g'></center>")


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
import random

random_number=random.randint(1,9)
app = Flask(__name__)


def make_bold(function):
    def wrap_bold():
        return "<b>" + function() + "</b>"
    return wrap_bold



@app.route('/')
# @make_bold
def hello_world():
    return '<h1> Guess a number between 0-9 </h1>' \
            '<img src="https://media.giphy.com/media/YRtLgsajXrz1FNJ6oy/giphy.gif" />'

@app.route("/<int:guess>")
def say_result(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)

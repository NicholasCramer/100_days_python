from flask import Flask
import random

rand_number = random.randint(0, 9)
print(rand_number)

LOW_URL = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
HIGH_URL = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
CORRECT_URL = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
WELCOME_IMAGE = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           f"<img src='{WELCOME_IMAGE}'/>"


@app.route('/<int:guess>')
def guess_number(guess):
    if guess > rand_number:
        return "<h1 style='color: red'>Too high, try again!</h1>" \
               f"<img src='{HIGH_URL}'/>"
    elif guess < rand_number:
        return "<h1 style='color: blue'>Too low, try again!</h1>" \
               f"<img src='{LOW_URL}'>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               f"<img src='{CORRECT_URL}'/>"


if __name__ == "__main__":
    app.run(debug=True)

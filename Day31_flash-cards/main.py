from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
dict_entry = {}
word_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_english_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")


# ---------------------------- Random Word -------------------------------- #

def next_word():
    global dict_entry, flip_timer
    window.after_cancel(flip_timer)
    dict_entry = random.choice(word_dict)
    language = list(dict_entry.keys())[0]
    canvas.itemconfig(word_language, text=language, fill="black")
    random_word = dict_entry[language]
    canvas.itemconfig(word, text=random_word, fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)


# ---------------------------- Flip Card ---------------------------------- #

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    language = list(dict_entry.keys())[1]
    canvas.itemconfig(word_language, text=language, fill="white")
    canvas.itemconfig(word, text=dict_entry[language], fill="white")


# -------------------- Remove known word from dict ------------------------- #

def is_known():
    word_dict.remove(dict_entry)
    new_data = pandas.DataFrame(word_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


# ------------------------------ UI --------------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

x_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="images/right.png")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
word_language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

unknown_button = Button(image=x_image, highlightthickness=0, command=next_word)
unknown_button.grid(column=0, row=1)
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_word()

window.mainloop()

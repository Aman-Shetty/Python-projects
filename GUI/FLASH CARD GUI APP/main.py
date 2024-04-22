import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
words ={}
current_word = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")



def translate():
    canvas.itemconfig(canvas_image, image=english)
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_word["English"], fill="white")


def next_word():
    global current_word, Timer
    window.after_cancel(Timer)
    current_word = random.choice(words)
    canvas.itemconfig(canvas_image, image=french)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill='black')
    Timer = window.after(3000, translate)

def Is_known():
    words.remove(current_word)
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_word()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

Timer = window.after(3000, next_word)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
french = PhotoImage(file="./images/card_front.png")
english = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 270, image=french)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

no = PhotoImage(file="./images/wrong.png")
wrong = Button(image=no, highlightthickness=0, bg=BACKGROUND_COLOR, command=translate)
wrong.grid(column=0, row=1)

yes = PhotoImage(file="./images/right.png")
right = Button(image=yes, highlightthickness=0, bg=BACKGROUND_COLOR, command=Is_known)
right.grid(column=1, row=1)

next_word()

window.mainloop()

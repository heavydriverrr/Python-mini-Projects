from tkinter import *
import pandas as pd
import random

# ---------------------------- COLORS & CONSTANTS ------------------------------- #
BACKGROUND = "#F0EAD6"
CARD_FRONT = "images/card_front.png"
CARD_BACK = "images/card_back.png"
FONT_LANG = ("Helvetica", 40, "italic")
FONT_WORD = ("Helvetica", 60, "bold")

# ---------------------------- DATA LOADING ------------------------------------- #
current_vocab = {}
words_remaining = {}

try:
    vocab_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    vocab_df = pd.read_csv("data/german-words.csv")

words_remaining = vocab_df.to_dict(orient="records")

# ---------------------------- FUNCTIONALITY ------------------------------------ #

def show_next_word():
    global current_vocab, flip_timer
    window.after_cancel(flip_timer)
    current_vocab = random.choice(words_remaining)
    canvas.itemconfig(card_img, image=front_image)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_vocab["German"], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_img, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_vocab["English"], fill="white")

def mark_known():
    words_remaining.remove(current_vocab)
    pd.DataFrame(words_remaining).to_csv("data/words_to_learn.csv", index=False)
    show_next_word()

# ---------------------------- UI SETUP ----------------------------------------- #
window = Tk()
window.title("Word Wizard")
window.config(padx=60, pady=60, bg=BACKGROUND)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND, highlightthickness=0)
front_image = PhotoImage(file=CARD_FRONT)
back_image = PhotoImage(file=CARD_BACK)
card_img = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=FONT_LANG)
card_word = canvas.create_text(400, 263, text="", font=FONT_WORD)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, bd=0, command=show_next_word)
wrong_btn.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, bd=0, command=mark_known)
right_btn.grid(row=1, column=1)

show_next_word()
window.mainloop()

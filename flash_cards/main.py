from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Arial'
LANGUAGE = 'French'
to_learn = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except:
    og_data = pandas.read_csv('data/french_words.csv')
    to_learn = og_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

current_card = {}

window = Tk()
window.title('Flashy')
window.minsize(width=800, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#------------------------NEXT CARD----------------------#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(language_text, fill='black', text=LANGUAGE)
    canvas.itemconfig(word_text, fill='black', text=current_card['French'])
    flip_timer = window.after(3000, func=flip_card)

    # df = pandas.read_csv('data/french_words.csv')
    # random_word = df.sample()
    # french_word = random_word.iloc[0]['French']
    # english_word = random_word.iloc[0]['English']
    # # word_lst = df['French'].tolist()
    # word_tuple = (french_word, english_word)
    # canvas.itemconfig(word_text, text=word_tuple[0])
    # return(word_tuple)

#------------------------FLIP CARD----------------------#

def flip_card():


    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(language_text, fill='white', text='English')
    canvas.itemconfig(word_text, fill='white', text=current_card['English'])
    # window.after_cancel()

#------------------------SAVE LIST----------------------#

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file='images/card_back.png')
card_front_img = PhotoImage(file='images/card_front.png')
canvas_image = canvas.create_image(410, 273, image=card_front_img)
language_text = canvas.create_text(400, 150, text=LANGUAGE, fill='black', font=(FONT_NAME, 40, 'italic'))
word_text = canvas.create_text(400, 263, text=LANGUAGE, fill='black', font=(FONT_NAME, 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2, sticky="EW")

# Buttons
left_button_img = PhotoImage(file="images/wrong.png")
left_button = Button(image=left_button_img, highlightthickness=0, command=next_card)
left_button.grid(column=0,row=1)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(column=1,row=1)

next_card()

window.mainloop()
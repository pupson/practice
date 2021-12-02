from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 8
check = "✔"
timer = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    checkmarks.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_seconds = count % 60

    canvas.itemconfig(timer_text, text=f'{count_min:02}:{count_seconds:02}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += check
        checkmarks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

def test(thing):
    print(thing)

window.after(1000, test, 'hello')

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)
# canvas.pack()

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 55, 'bold'))
title_label.grid(column=1, row=0)

button1 = Button(text="Start", highlightthickness=0, command=start_timer)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", highlightthickness=0, command=reset_timer)
button2.grid(column=2, row=2)

checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()
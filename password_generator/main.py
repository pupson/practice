from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

FONT_NAME = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    pass_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list.extend([choice(symbols) for char in range(randint(2, 4))])
    password_list.extend([choice(numbers) for char in range(randint(2, 4))])

    shuffle(password_list)
    password = ''.join(password_list)
    pass_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_input = web_entry.get()
    email_input = email_entry.get()
    pass_input = pass_entry.get()

    if len(web_input) == 0 or len(pass_input) == 0:
        messagebox.showwarning(title="Entry box empty", message='Please enter a valid email or password')
    else:
        is_ok = messagebox.askokcancel(title=web_input, message=f'Inputting Email: {email_input}\n Password: {pass_input}')
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f'{web_input} | {email_input}| {pass_input} \n')

            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website: ', font=(FONT_NAME, 10, 'bold'))
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username: ', font=(FONT_NAME, 10, 'bold'))
email_label.grid(column=0, row=2)

pass_label = Label(text='Password: ', font=(FONT_NAME, 10, 'bold'))
pass_label.grid(column=0, row=3)

gen_button = Button(text="Generate Password", command=pass_gen)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

#Entries
web_entry = Entry()
web_entry.focus()
#Gets text in entry
web_input = web_entry.get()
web_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

email_entry = Entry()
email_entry.insert(END, 'your_email@gmail.com')
email_input = email_entry.get()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

pass_entry = Entry()
pass_input = pass_entry.get()
pass_entry.grid(column=1, row=3, sticky="EW")


window.mainloop()
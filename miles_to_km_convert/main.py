from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=100, height=100)
window.config(padx=10, pady=10)


#Labels
label = Label(text="is equal to")
label.grid(column=0, row=1)
label.config(padx=10, pady=10)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label1.config(padx=10, pady=10)

label2 = Label(text="Km")
label2.grid(column=2, row=1)
label2.config(padx=10, pady=10)

label3 = Label(text="0")
label3.grid(column=1, row=1)
label3.config(padx=10, pady=10)


def convert():
    miles = entry.get()
    kms = round(float(miles) * 1.609344, 2)
    label3.config(text=kms)

#Entries
entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
miles = entry.get()
entry.grid(column=1, row=0)

# Buttons
button1 = Button(text="Convert", command=convert)
button1.grid(column=1, row=2)



window.mainloop()
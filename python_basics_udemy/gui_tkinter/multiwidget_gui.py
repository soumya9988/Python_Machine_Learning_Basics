from tkinter import *

window = Tk()


def convert_temp():
    gms = float(kg_value.get()) * 1000
    text_gms.insert(END, gms)

    pound = float(kg_value.get()) * 2.20642
    text_pounds.insert(END, pound)

    ounce = float(kg_value.get()) * 35.274
    text_ounce.insert(END, ounce)


label_kg = Label(window, text='Kg')
label_kg.grid(row=0, column= 0)

kg_value = StringVar()
entry_kg = Entry(window, textvariable=kg_value)
entry_kg.grid(row=0, column= 3)

convert = Button(window, text='Convert', command=convert_temp)
convert.grid(row=0, column=10)

text_gms = Text(window, height=1, width=20)
text_gms.grid(row=2, column= 0)

text_gms = Text(window, height=1, width=20)
text_gms.grid(row=2, column= 0)

text_pounds = Text(window, height=1, width=20)
text_pounds.grid(row=2, column= 3)

text_ounce = Text(window, height=1, width=20)
text_ounce.grid(row=2, column= 10)

window.mainloop()
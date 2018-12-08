import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

# Create the application window
window = tk.Tk()

# Create a label
my_label = ttk.Label(window, text="Hello World!")
my_label.grid(row=1, column=1)

# Simple dialog box
name = simpledialog.askstring('Info', 'What is your name', parent=window)
print('Your name is', name)
age = simpledialog.askinteger('Info', 'Please enter your age!', parent= window)
print('Your age is:', age)

# Display messages
messagebox.showwarning('Warning','Hello World is displayed. Close it')
like = messagebox.askyesnocancel('Message', 'Do you like Python?')
print(like)
answer = messagebox.askretrycancel('Question', 'Are you able to close this window?')
print(answer)

# button
b1 = tk.Button(window, text='OK')
# File choosing
file_name = filedialog.askopenfilename()
print(file_name)
# Start the GUI event loop
window.mainloop()
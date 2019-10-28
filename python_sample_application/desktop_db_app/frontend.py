"""
A program that stores the book store information:
    Title, Author, ISBN, Year

User can:
1. View all entries
2. Update the entries
3. Search an entry
4. Add an entry
5. Delete an entry
6. Exit program

"""

from tkinter import *
import backend

window = Tk()


def get_selected_row():
    try:
        global selected_tuple
        index = lb.curselection()[0]
        selected_tuple = lb.get(index)

        entry_title.delete(0, END)
        entry_title.insert(END, selected_tuple[1])
        entry_author.delete(0, END)
        entry_author.insert(END, selected_tuple[2])
        entry_year.delete(0, END)
        entry_year.insert(END, selected_tuple[3])
        entry_isbn.delete(0, END)
        entry_isbn.insert(END, selected_tuple[4])

    except IndexError:
        pass


def view_command():
    lb.delete(0, END)
    for item in backend.view():
        lb.insert(END, item)


def search_command():
    lb.delete(0, END)
    for item in backend.search(title_value.get(),
                               author_value.get(),
                               year_value.get(),
                               isbn_value.get()):
        lb.insert(END, item)


def add_command():
    backend.insert( title_value.get(),
                    author_value.get(),
                    year_value.get(),
                    isbn_value.get())
    lb.delete(0, END)
    lb.insert(END,(title_value.get(),author_value.get(), year_value.get(), isbn_value.get()))


def delete_command():
    get_selected_row()
    backend.delete(selected_tuple[0])
    view_command()


def update_command():
    get_selected_row()
    backend.update(selected_tuple[0],
                   selected_tuple[1], # Title
                   selected_tuple[2], # Author
                   selected_tuple[3], # Year
                   selected_tuple[4]) # ISBN
    view_command()


l_title = Label(window, text='Title')
l_title.grid(row=0, column=0)

title_value = StringVar()
entry_title = Entry(window, textvariable=title_value)
entry_title.grid(row=0, column= 1)

l_author = Label(window, text='Author')
l_author.grid(row=0, column=2)

author_value = StringVar()
entry_author = Entry(window, textvariable=author_value)
entry_author.grid(row=0, column= 3)

l_year = Label(window, text='Year')
l_year.grid(row=1, column=0)

year_value = StringVar()
entry_year = Entry(window, textvariable=year_value)
entry_year.grid(row=1, column=1)

l_isbn = Label(window, text='ISBN')
l_isbn.grid(row=1, column=2)

isbn_value = StringVar()
entry_isbn = Entry(window, textvariable=isbn_value)
entry_isbn.grid(row=1, column= 3)

lb = Listbox(window, height= 6, width=35)
lb.grid(row=2, column=0, rowspan=6, columnspan=2)

sb =  Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

lb.configure(yscrollcommand= sb.set)
sb.configure(command=lb.yview)

lb.bind('<<getSelectedRow>>', get_selected_row)

b1 = Button(window, text='View All', width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search Entry', width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update Entry', width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete Entry', width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=12)
b6.grid(row=7, column=3)


window.mainloop()

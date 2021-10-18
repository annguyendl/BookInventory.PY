from tkinter import *
from BookInvBE import BookDB

book=BookDB("books.db")

class Window(object):

    def __init__(self, window):
        self.window=window
        self.window.wm_title("Book Store")

        l1=Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2=Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3=Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4=Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        self.title_text=StringVar()
        self.e1=Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text=StringVar()
        self.e2=Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text=StringVar()
        self.e3=Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text=StringVar()
        self.e4=Entry(window, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        self.list1=Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.sb1=Scrollbar(window)
        self.sb1.grid(row=2, column=2, rowspan=6)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        b1=Button(window, text='View all', width=12, command=self.view_cmd)
        b1.grid(row=2, column=3)

        b2=Button(window, text='Search entry', width=12, command=self.search_cmd)
        b2.grid(row=3, column=3)

        b3=Button(window, text='Add entry', width=12, command=self.add_cmd)
        b3.grid(row=4, column=3)

        b4=Button(window, text='Update', width=12, command=self.update_cmd)
        b4.grid(row=5, column=3)

        b5=Button(window, text='Delete', width=12, command=self.delete_cmd)
        b5.grid(row=6, column=3)

        b6=Button(window, text='Close', width=12, command=window.destroy)
        b6.grid(row=7, column=3)

        self.view_cmd()

    def view_cmd(self):
        self.list1.delete(0, END)
        for row in book.viewall():
            self.list1.insert(END, row)

    def search_cmd(self):
        self.list1.delete(0, END)
        result=book.search(title=self.title_text.get(), author=self.author_text.get(), year=self.year_text.get(), isbn=self.isbn_text.get())
        for row in result:
            self.list1.insert(END, row)

    def add_cmd(self):
        self.list1.delete(0, END)
        book.insert(title=self.title_text.get(), author=self.author_text.get(), year=self.year_text.get(), isbn=self.isbn_text.get())
        self.view_cmd()

    def get_selected_row(self, event):
        try:
            index=self.list1.curselection()[0]
            self.selected_tuble=self.list1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, self.selected_tuble[1])
            self.e2.delete(0, END)
            self.e2.insert(END, self.selected_tuble[2])
            self.e3.delete(0, END)
            self.e3.insert(END, self.selected_tuble[3])
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_tuble[4])
        except IndexError:
            pass

    def delete_cmd(self):
        book.delete(self.selected_tuble[0])
        self.view_cmd()

    def update_cmd(self):
        book.update(id=self.selected_tuble[0], title=self.title_text.get(), author=self.author_text.get(), year=self.year_text.get(), isbn=self.isbn_text.get())
        self.view_cmd()

window = Tk()
Window(window)
window.mainloop()
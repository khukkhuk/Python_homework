from tkinter import *
from tkinter import messagebox
from test import *


class My:
    def __init__(self, master):
        self.master = master 
        frame = Frame(self.master)
        add = Button(frame, text = "add",
                         command = self.add_window)
        add.pack(side=TOP,expand=1,fill="both")
        
        show = Button(frame, text = "show",
                         command = self.show_window)
        show.pack(side=TOP,expand=1,fill="both")
        
        find = Button(frame, text = "find",
                         command = self.find_window)
        find.pack(side=TOP,expand=1,fill="both")
        

        
        #delete = tk.Button(frame, text = "delete",
         #                command = self.delete_window)
        #delete.pack()

        squit = Button(frame, text = "Exit",
                          command = self.master.destroy)
        
        
        squit.pack(side=TOP,expand=1,fill="both")
        frame.pack()
        
    def add_window(self):
        self.new = Toplevel(self.master)
        add(self.new)
        
    def show_window(self):
        self.new = Toplevel(self.master)
        show(self.new)
        
    def find_window(self):
        self.new = Toplevel(self.master)
        find(self.new)
        
    def delete_window(self):
        self.new = Toplevel(self.master)
        delete(self.new)

root = Tk()
app = My(root)
root.mainloop()

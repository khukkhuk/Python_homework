from tkinter import *
def insert():
    name = e1.get()
    sur = e2.get()
    lb.insert(END,name)
    ls.insert(END,sur)
    e1.delete(0,END)
    e2.delete(0,END)
    
def delete():
    index = lb.index(lb.curselection())
    lb.delete(index,index)
    ls.delete(index,index)
    e1.delete(0,END)
    e2.delete(0,END)

def show():
    name = lb.get(lb.curselection())
    index = lb.index(lb.curselection())
    lastname=ls.get(index)
    e1.delete(0,END)
    e2.delete(0,END)
    e1.insert(0,name)
    e2.insert(0,lastname)
    
root = Tk()
ls = []
Label(root,text='name').grid(row=0)
e1 = Entry(root)
e1.grid(row=0,column=1)

Label(root,text='surname').grid(row=1)
e2 = Entry(root)
e2.grid(row=1,column=1)

Button(root,text="add",command=insert).grid(row=2,column=0)
Button(root,text="delete",command=delete).grid(row=2,column=1)
Button(root,text="show",command=show).grid(row=3,column=1)

lb = Listbox(root,selectmode=SINGLE,width=20,height=5)
ls = Listbox(root)
lb.grid(row=0,column=2,rowspan=3,columnspan=3)
root.mainloop()







from tkinter import *
name = []
gender = []
avg_age = []

def displayInput():
    e1.delete(0,END)
    e1.insert(0,name[Lb1.curselection()[0]])

def push():
    print("-----ADD-----")
    name.append(e1.get())
    gender.append(genderOption.get())
    avg_age.append(avgAge.get())
    Lb1.insert(END,e1.get())
    print("name",name)
    print("gender",gender)
    print("avg_age", avg_age)

def pop():
    print("-----DELETE-----")
    kk=Lb1.curselection()
    name.pop(kk[0])
    gender.pop(kk[0])
    avg_age.pop(kk[0])
    Lb1.delete(Lb1.curselection()[0])
    print("name",name)
    print("gender",gender)
    print("avg_age", avg_age)
    

root = Tk()

genderOption = StringVar()
genderOption.set("Men")
OptionList = [
    "Age 15-20",
    "Age 21-25",
    "Age 26-30",
    "Age 30 up"
]
avgAge = StringVar()
avgAge.set(OptionList[0])

l1 = Label(root, text="Name : ",bg='lightpink')
l2 = Label(root, text="Gender : ",bg='lightgreen')
l3 = Label(root, text="Avg Age : ",bg='yellow')

l1.grid(row=0, column=0,sticky=W) #columnspan=1 sticky=E+W
l2.grid(row=1, column=0,sticky=W)
l3.grid(row=2, column=0,sticky=W)

e1 = Entry(root) #bd2
e2 = Radiobutton(root, text="Men", value="Men", variable=genderOption,bg='lightblue')
e3 = Radiobutton(root, text="Women", value="Women", variable=genderOption,bg='lightpink')
e4 = OptionMenu(root, avgAge, *OptionList)

e1.grid(row=0, column=1, columnspan = 2)
e2.grid(row=1, column=1)
e3.grid(row=1, column=2)
e4.grid(row=2, column=1, columnspan = 2)

b1 = Button(root,text="ADD", command=push,bg='lightblue')
b2 = Button(root,text="DELETE", command=pop,bg='red')

b1.grid(row = 3, column = 0, columnspan = 1, sticky='e') 
b2.grid(row = 3, column = 2, columnspan = 1, sticky='w') 

Lb1 = Listbox(root, selectmode=SINGLE)
Lb1.grid(row = 0, column = 3, 
       columnspan = 1, rowspan = 5, padx = 5, pady = 5)

scrollbar = Scrollbar(command=Lb1.yview, orient=VERTICAL)
scrollbar.grid(row = 0, column = 4, 
       columnspan = 5, rowspan = 5, padx = 5, pady = 5, sticky='ns')
Lb1.configure(yscrollcommand=scrollbar.set)

Lb1.bind("<<ListboxSelect>>",lambda event:displayInput())




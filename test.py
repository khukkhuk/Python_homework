#import tkinter as tk
from tkinter import messagebox
from tkinter import *

name = ['khuk','beam','bam','khuk']
tel = ['1','2','3','4']
class add:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.Var1 = StringVar()
        self.Var2 = StringVar()
        frame = Frame(self.master)

        f1 =  Frame(frame)
        
        Label(f1, text= "Name").grid(row="0",column="0")
        
        E1 =  Entry(f1, textvariable=self.Var1)
        E1.grid(row="0",column="1")
        
        Label(f1, text = "Tel_number").grid(row="1",column="0")
        
        E2 =  Entry(f1, textvariable=self.Var2)
        E2.grid(row="1",column="1")
        
        f1.pack()
        
        show =  Button(frame, text = "add",
                command = lambda:self.function_add())
        show.pack(side= LEFT,expand=1,fill="both")
        
        self.quit =  Button(frame, text = "Exit",
                              command = self.master.destroy)
        self.quit.pack(side= LEFT,expand=1,fill="both")
        
        frame.pack()
        
    def function_add(self):
        Var1 = self.Var1.get()
        Var2 = self.Var2.get()
        index = len(tel)
        status = "";
        for x in range(index):
            if Var2 == tel[x]:
                status = "FAIL"
            
        if status == "FAIL" :
            messagebox.showwarning("ShowWarning","Already have this number.")

        else:
            END = len(name)
            END = END + 1
            name.insert(END,Var1)
            tel.insert(END,Var2)
            messagebox.showinfo("ShowInfo","Add Success")
           
class show:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        frame =  Frame(self.master)
        f1 =  Frame(frame)
        Label(f1,text="Show Data").grid(row=0,column=0)
        data = ""
        total = 0
        a1 = int(len(name))
        for x in range(a1):
            
            total = total +1
            
            data = data + str(total)+". "+str(name[x])+" , "+str(tel[x])+"\n"
            
            
        print(data)
        total = "Total Record : "+str(total)
        
        Label(f1,text=data).grid(row=1,column=0)
        Label(f1,text=total).grid(row=2,column=0)
        f1.pack()
        frame.pack()

class find:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        frame =  Frame(self.master)
        self.Var1 =  StringVar()
        self.Var2 =  StringVar()

        f1 =  Frame(frame)
        
        Label(f1, text= "Name").grid(row="0",column="0")
        
        E1 =  Entry(f1, textvariable=self.Var1)
        E1.grid(row="1",column="0")

        show =  Button(frame, text = "find name",
                command = lambda:self.find_name())
        show.pack(side= BOTTOM,expand=1,fill="both")
        
        f1.pack()
        
        f2 =  Frame(frame)
        Label(f2, text = "Tel_number").grid(row="2",column="0")
        
        E2 =  Entry(f2, textvariable=self.Var2)
        E2.grid(row="3",column="0")

        
        show =  Button(frame, text = "find number",
                command = lambda:self.find_num())
        show.pack(side= BOTTOM,expand=1,fill="both")
        
        f2.pack()
        
        self.quit =  Button(frame, text = "exit",
                              command = self.master.destroy)
        self.quit.pack(side= BOTTOM,expand=1,fill="both")
        
        frame.pack()
    def find_num(self):
        Var2 = self.Var2.get()
        index = tel.index(Var2)
        if index != "" :
            index = tel.index(Var2)
            messagebox.showinfo("ShowInfo","Number : "+str(Var2)+"\n"
                            "name : "+str(name[index]))
        else:
            messagebox.showwarning("ShowWarning","Not found")
    def find_name(self):
        Var1 = self.Var1.get()
        index  = len(name)
        data = ""
        n = 1
        for x in range(index):
            
            if Var1 == name[x]:
                data = data + str(n)+". "+str(name[x])+" , " +str(tel[x])+"\n" 
                n = int(n)
                n = n + 1


        if data != "" :
            index = name.index(Var1)
            messagebox.showinfo("ShowInfo",data)
        else:
            messagebox.showwarning("ShowWarning","Not found")
        
class delete:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        frame =  Frame(self.master)
        

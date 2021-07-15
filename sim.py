import tkinter as tk

H = 500
W = 800

root = tk.Tk()
canvas = tk.Canvas(root, height=H, width=W)
canvas.pack()

labelR1 = tk.Label(text='R1',font=('Courier',10))
labelR1.place(relx=0.05,rely=0.05)

labelR2 = tk.Label(text='R2',font=('Courier',10))
labelR2.place(relx=0.05,rely=0.12)

label1v = tk.Label(text='Volt1',font=('Courier',10))
label1v.place(relx=0.04,rely=0.19)

R1_input = tk.Entry(font=('Courier', 10))
R1_input.place(relx=0.1,rely=0.05,relwidth=0.5, relheight=0.05)

R2_input = tk.Entry(font=('Courier', 10))
R2_input.place(relx=0.1,rely=0.12,relwidth=0.5, relheight=0.05)

v1_input = tk.Entry(font=('Courier', 10))
v1_input.place(relx=0.1,rely=0.19,relwidth=0.5, relheight=0.05)

button = tk.Button( text='ตกลง', font=40,command=lambda:show(R1_input.get(),R2_input.get(),v1_input.get()))
button.place(rely=0.05,relx=0.7, relwidth=0.2, relheight=0.1)

lower_frame = tk.Frame(root, bg= '#000000', bd=1)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 10), anchor='nw', justify='left') # ไว้แสดงข้อความบน lower_frame
label.place(relwidth=1, relheight=1)

def show(R1,R2,V):
    s = "อนุกรม\n"
    r1 = float(R1) * 1000
    r2 = float(R2) * 1000
    rt = (r1+r2)/1000
    it = float(V) / rt
    i1=i2=it
    v1 = (it*r1)/1000
    v2 = (it*r2)/1000
    if(v1 == v2):
        s = s + "VT = V1,V2 = " + str(v2)+"V\n"
    else:
        s = s + "VT = "+str(it*rt)+ "\nV1 = " +str(v1) + "\nV2 = " + str(v2)+"\n"

    if(r1 == r2):
        s = s + "RT = R1,R2 = "+ str(r2/1000)+"\n"
    else:
        s = s + "RT = "+str(rt) + "\nR1 = " + str(r1/1000) + "\nR2 = "+ str(r2/1000)+"\n"

    if(i1 == i2):
        s = s + "IT = I1,I2 = " + str(i1)+"\n"
    else:
        s = s + "IT = "+str(it)+"\nI1 = "+str(i1)+"\nI2 = " + str(i2)+"\n"

    s = s + "ขนาน\n"

    r1 = float(R1) * 1000
    r2 = float(R2) * 1000
    rt = ((r1*r2)/(r1+r2))
    rt = rt*(10**-3)
    it=float(V)/(rt*1000)
    v1=v2=float(V)
    i1=v1/r1
    i2=v2/r2

    if(v1 == v2):
        s = s + "VT = V1,V2 = " + str(v2)+"V\n"
    else:
        s = s + "VT = "+str(it*rt)+ "\nV1 = " +str(v1) + "\nV2 = " + str(v2)+"\n"

    if(r1 == r2):
        s = s + "RT = R1,R2 = "+ str(r2/1000)+"\n"
    else:
        s = s + "RT = "+str(rt) + "\nR1 = " + str(r1/1000) + "\nR2 = "+ str(r2/1000)+"\n"

    if(i1 == i2):
        s = s + "IT = I1,I2 = " + str(i1)+"\n"
    else:
        s = s + "IT = "+str(it)+"\nI1 = "+str(i1)+"\nI2 = " + str(i2)+"\n"
        
    label.config(text=s)

root.mainloop()


import tkinter
w = tkinter.Tk()
w.title("abbb")
Menubar=tkinter.Menu(w,bg="white")
def addno():
    n1=int(num1.get())
    n2=int(num2.get())
    R=n1+n2
    textv.set(R)
def subno():
    n1=int(num1.get())
    n2=int(num2.get())
    R=n1-n2
    textv.set(R)
def mulno():
    n1=int(num1.get())
    n2=int(num2.get())
    R=n1+*n2
    textv.set(R)
def divno():
    n1=int(num1.get())
    n2=int(num2.get())
    R=n1/n2
    textv.set(R)
num1=tkinter.StringVar()
num2=tkinter.StringVar()
textv=tkinter.StringVar()    
fm=tkinter.Menu(Menubar,tearoff=0)
fm.add_command(label="save")
fm.add_command(label="new file")
fm.add_command(label="open")
Menubar.add_cascade(label="FILE",menu=fm)
fm=tkinter.Menu(Menubar,tearoff=0)
fm.add_command(label="cut")
fm.add_command(label="redo")
fm.add_command(label="undo")
Menubar.add_cascade(label="EDIT",menu=fm) 
fm=tkinter.Menu(Menubar,tearoff=0)
fm.add_command(label="selectall")
fm.add_command(label="copyline")
fm.add_command(label="add couser")
Menubar.add_cascade(label="FORMATE",menu=fm)
fm=tkinter.Menu(Menubar,tearoff=0)
fm.add_command(label="show command")
fm.add_command(label="tips and tricks")
fm.add_command(label="report issue")
Menubar.add_cascade(label="HELP",menu=fm)
e=tkinter.Entry(w,textvariable=num1).grid(row=0,column=1)
l=tkinter.Label(w,text="first NO").grid(row=0,column=0)
e2=tkinter.Entry(w,textvariable=num2).grid(row=2,column=1)
l2=tkinter.Label(w,text="Second Number").grid(row=2,column=0)
e3=tkinter.Entry(w,textvariable=textv).grid(row=4,column=1)
l3=tkinter.Label(w,text="Result").grid(row=4,column=0)
e1=tkinter.Entry(w).grid(row=6,column=0)
l1=tkinter.Button(w,text="Add").grid(row=6,column=0)
e4=tkinter.Entry(w).grid(row=6,column=1)
l4=tkinter.Button(w,text="sub").grid(row=6,column=1)
e5=tkinter.Entry(w).grid(row=6,column=2)
l5=tkinter.Button(w,text="mul").grid(row=6,column=2)
e6=tkinter.Entry(w).grid(row=6,column=3)
l6=tkinter.Button(w,text="div").grid(row=6,column=3)
w.config(menu=Menubar)

w.mainloop()
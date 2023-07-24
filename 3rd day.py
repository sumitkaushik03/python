import tkinter
w=tkinter.Tk()
#def addno():





l1=tkinter.Label(w,text="firstno").grid(row=0,column=0)
l2=tkinter.Label(w,text="secondno").grid(row=1,column=0)
e1=tkinter.Entry(w).grid(row=1,column=0)
e2=tkinter.Entry(w).grid(row=1,column=1)
b=tkinter.Entry(w,text="add").grid(row=0,column=2)
r=tkinter.label(w,text="result").grid(row=2,column=0)
w.mainloop()
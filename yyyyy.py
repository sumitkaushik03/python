from tkinter import*
w = Tk()
Menubar = Menu(w,bg="red")
fm=Menu(Menubar,tearoff=0)
Menubar.add.cascadee(label="file",menu=fm)
w.config(menu=menubar)
w.mainloop()
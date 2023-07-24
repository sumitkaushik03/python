from tkinter import*
from tkinter import messagebox
w=Tk()
def msg():messagebox.askyesno("info","submition succesfully")
def msg():messagebox.showinfo("info","submition succesfully")
def msg():messagebox.showerror("info","submition succesfully")
def msg():messagebox.showwarning("info","submition succesfully")
def msg():messagebox.askokcancel("info","submition succesfully")
def msg():messagebox.askretrycancel("info","submition succesfully")
b=Button(w,text="ok",command=msg).grid(row=0,column=0)
w.mainloop()
from tkinter import *
master = Tk()
p = Entry(master)
p.focus_set()
e = Entry(master)
e.pack()
p.pack()
h =Entry(master)
h.pack()
h.focus_set()
e.focus_set()


def callback():
    print(p.get())
    if p.get() == "+":
        print(int(e.get())+int(h.get()))
    elif p.get() == "-":
        print(int(e.get())-int(h.get()))
    elif p.get()=="*":
        print(int(e.get())*int(h.get()))
    elif p.get()=="/":
        print(int(e.get())/int(h.get()))
b = Button(master, text = "enter", width = 10, command = callback)
b.pack()

mainloop()

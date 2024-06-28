from tkinter import *

r = Tk()
r.geometry("590x480")
r.title("Calculator")
r.configure(bg="black")
e = Entry(r, width=50, borderwidth=5,font=15)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

def onClick(num):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(num))
def onClear():
    e.delete(0,END)
def but_ad():
    fn=e.get()
    global f,q
    q='+'
    f=int(fn)
    e.delete(0,END)
def but_sub():
    fn=e.get()
    global f,q
    q='-'
    f=int(fn)
    e.delete(0,END)
def but_mul():
    fn=e.get()
    global f,q
    q='*'
    f=int(fn)
    e.delete(0,END)
def but_div():
    fn=e.get()
    global f,q
    q='/'
    f=int(fn)
    e.delete(0,END)

def but_eq():
    sn=e.get()
    e.delete(0,END)
    if(q=="+"):
        e.insert(0,f+int(sn))
    elif (q == "-"):
        e.insert(0, f - int(sn))
    elif (q == "*"):
        e.insert(0, f * int(sn))
    elif (q == "/"):
        e.insert(0, f / int(sn))

button1 = Button(r, text="1", font=5, padx=35, pady=15, command= lambda: onClick(1))
button2 = Button(r, text="2", font=5,padx=35, pady=15, command= lambda: onClick(2))
button3 = Button(r, text="3", font=5,padx=35, pady=15, command= lambda: onClick(3))
button4 = Button(r, text="4", font=5,padx=35, pady=15, command= lambda: onClick(4))
button5 = Button(r, text="5", font=5,padx=35, pady=15, command= lambda: onClick(5))
button6 = Button(r, text="6", font=5,padx=35, pady=15, command= lambda: onClick(6))
button7 = Button(r, text="7", font=5,padx=35, pady=15, command= lambda: onClick(7))
button8 = Button(r, text="8", font=5,padx=35, pady=15, command= lambda: onClick(8))
button9 = Button(r, text="9", font=5,padx=35, pady=15, command= lambda: onClick(9))
button0 = Button(r, text="0", font=5,padx=35, pady=15, command= lambda: onClick(0))

button_add = Button(r, text="+",font=5, padx=39, pady=15, command= but_ad)
button_sub = Button(r, text="-",font=5, padx=39, pady=15, command= but_sub)
button_mul = Button(r, text="*",font=5, padx=39, pady=15, command= but_mul)
button_div = Button(r, text="/",font=5, padx=39, pady=15, command= but_div)
button_eql = Button(r, text="=",font=5, padx=108, pady=15, command= but_eq)
button_clr = Button(r, text="Clear",font=5, padx=235, pady=15,command= onClear)

button0.grid(row=4,column=0,pady=5)
button1.grid(row=3,column=0,pady=5)
button2.grid(row=3,column=1,pady=5)
button3.grid(row=3,column=2,pady=5)

button4.grid(row=2,column=0,pady=5)
button5.grid(row=2,column=1,pady=5)
button6.grid(row=2,column=2,pady=5)

button7.grid(row=1,column=0,pady=5)
button8.grid(row=1,column=1,pady=5)
button9.grid(row=1,column=2,pady=5)

button_add.grid(row=1,column=3,pady=5)
button_sub.grid(row=2,column=3,pady=5)
button_mul.grid(row=3,column=3,pady=5)
button_div.grid(row=4,column=3,pady=5)
button_eql.grid(row=4,column=1,columnspan=2,pady=5)

button_clr.grid(row=5,column=0,columnspan=4,pady=5)

r.mainloop()

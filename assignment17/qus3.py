# Q3. Create a frame using tkinter with any label text and two buttons.
# One to exit and other to change the label to some other text.

from tkinter  import *
import sys


 def exit():
     sys.exit()


 def show():
     if(t.get()==0):
        n.set("spy power")
        t.set(1)
     else:
         n.set("Hello Java")
         t.set(0)

 def display(r):
     print(r)


 root =Tk()
 t = IntVar()
 t.set(0)
- n=StringVar()
 n.set("Hello World")
 root.title("spy world")
 root.geometry("205x250")
 root.resizable(True,False)
 root.minsize(200,200)
 root.maxsize(300,300)
 l = Label(root, textvariable=n, width=50, bg="dodgerblue", fg="white")
 l.pack()
 b=Button(root,text="Exit",width=25,bg="green",fg="yellow",command=exit)
 b.pack()

 b1=Button(root,text="Change",width=25,bg="green",fg="yellow",command=show)
 b1.pack()

 b2= Button(root, text="Hello", command=lambda : display(10))
 b2.pack()

 root.mainloop()

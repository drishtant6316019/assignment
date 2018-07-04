# Q1. Write a python program using tkinter interface to
# write Hello World and a exit button that closes the interface.
 from tkinter  import *
 import sys
 def exit():
     sys.exit()
 w=Tk()
 l=Label(w,text="Hello World",width=50,bg="green",fg="red")
 l.pack()
 b=Button(w,text="Exit",width=25,bg="yellow",command=exit)
 b.pack()
 w.mainloop()
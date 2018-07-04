# Q2. Write a python program to in the same interface as above
# # and create a action when the button is click it will display
# # some text.
 from tkinter  import *
 def disp():
     l=Label(w,text="Hello World",width=50,bg="green",fg="red")
     l.pack()
 w=Tk()
 b=Button(w,text="Click!",width=25,bg="yellow",command=disp)
 b.pack()
 w.mainloop()

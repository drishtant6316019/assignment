# Q4. Write a python program using tkinter interface to
# take an input in the GUI program and print it.
 from tkinter import *
 def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
 w = Tk()
 Label(w, text="First Name").grid(row=0)
 Label(w, text="Last Name").grid(row=1)

 e1 = Entry(w)
 e2 = Entry(w)

 e1.grid(row=0, column=1)
 e2.grid(row=1, column=1)
 b=Button(w, text='Quit', command=w.quit).grid(row=3, column=0, sticky=W,pady=4,)

 c=Button(w, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

 mainloop( )

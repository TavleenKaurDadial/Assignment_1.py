'''1) Implement the tkinter and webbrowser module

2) create a gui for taking input from the user and 
create a button to navigate to a browser site.

3) Also display the user entered text in the command prompt
 with message of navigating to "..." whichever site you chooses'''

import tkinter as tk
import webbrowser as wb
ob=tk.Tk(className="Assignment10")
e=tk.Entry(ob,font=("Times New Roman",30),width=30)
e.grid()

def display():
    s=e.get()
    print("navigating to-> www.udemy.com/courses/search?q=")
    print(s)
    wb.open("www.udemy.com/courses/search?q="+s)

b=tk.Button(ob,text="Search",
            font=("Times New Roman",30),
            bg="pink",
            activebackground="purple",
            command=display)

b1=tk.Button(ob,
             text="Close",
             font=("Times New Roman",30),
             command=ob.destroy)


b.grid(row=5,column=0)
b1.grid(row=6,column=0)
ob.mainloop()



#ASSIGNMENT 12

from recharge import *
from DTH import *
from travel import *
from tkinter import *
import webbrowser as wb
root=Tk()
root.title("Paytm Tavleen")



def signin():
    wb.open("https://accounts.paytm.com/register#!/signup")

headerl=Label(root,text="PayTm",foreground='dark blue',
                font=("Bahnschrift SemiLight SemiConde ",50))
headerl.grid(row=0,column=0)
b=Button(root,text="SignIn",foreground="white",background="light blue",
         font=("Bahnschrift SemiLight SemiConde",30),command=signin
         )
b.place(x=1200,y=0)

l=Label(root,text="_________________________________________________________________________________________________________________________________________________________________",
        foreground="blue",
        font=("Calibri",30)
        )
l.place(x=0,y=80)


l1=Label(root,text="Recharge",foreground="dark blue",
         font=("Bahnschrift SemiLight SemiConde",25))
l1.place(x=25,y=150)
b1=Button(root,text="Prepaid/Postpaid",
          background="light blue",foreground="white",
          font=("Calibri",20),
          command=New_Window)
b1.place(x=300,y=150)


l2=Label(root,text="DTH or TV",foreground="dark blue",
        font=("Bahnschrift SemiLight SemiConde",25))
l2.place(x=25,y=250)
b2=Button(root,text="DTH",foreground="white",background="light blue",
          font=("Calibri",20),command=New_DTH)
b2.place(x=300,y=250)


l3=Label(root,text="Travel",foreground="dark blue",
        font=("Bahnschrift SemiLight SemiConde",25))
l3.place(x=25,y=350)
b3=Button(root,text="Metro",foreground="white",background="light blue",
          font=("Calibri",20),command=New_Travel)
b3.place(x=300,y=350)









root.mainloop()

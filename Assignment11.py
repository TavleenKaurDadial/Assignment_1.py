'''Create a gui based form to take input from the user 
and then navigate to the particular site from where 
the user came to know about the content

for example:
create a form where the user is enquiring about the respective course
and in the form there is an option for asking where the user came to know about it,
 for eg: instagram ads or YouTube ads

and then when clicking the submit button
take the user to the faq page of that site'''

import webbrowser as wb
import tkinter as tk
root=tk.Tk()
root.title("Assignment11 Tavleen")

headerl=tk.Label(root,text="COLLEGE REGISTRATION FORM",
           font=("Times New Roman",30))
headerl.grid(row=0,column=1)

l1=tk.Label(root,text="NAME:",
            font=("Ariel",15))
l1.grid(row=1,column=0)
e1=tk.Entry(root,font=("Ariel",15),
            width=30)
e1.grid(row=1,column=1)


l2=tk.Label(root,text="COURSE:",
            font=("Ariel",15))
l2.grid(row=2,column=0)
e2=tk.Entry(root,font=("Ariel",15),
            width=30)
e2.grid(row=2,column=1)


l3=tk.Label(root,text="SEMESTER:",
            font=("Ariel",15))
l3.grid(row=3,column=0)
e3=tk.Entry(root,font=("Ariel",15),
            width=30)
e3.grid(row=3,column=1)


l4=tk.Label(root,text="CONTACT NO:",
            font=("Ariel",15))
l4.grid(row=4,column=0)
e4=tk.Entry(root,font=("Ariel",15),
            width=30)
e4.grid(row=4,column=1)


l5=tk.Label(root,text="EMAIL ID:",
            font=("Ariel",15))
l5.grid(row=5,column=0)
e5=tk.Entry(root,font=("Ariel",15),
            width=30)
e5.grid(row=5,column=1)


l6=tk.Label(root,text="ADDRESS:",
            font=("Ariel",15))
l6.grid(row=7,column=0)
e6=tk.Entry(root,font=("Ariel",15),
            width=30)
e6.grid(row=7,column=1)


l7=tk.Label(root,text="SSC PERCENTAGE:",
            font=("Ariel",15))
l7.grid(row=8,column=0)
e7=tk.Entry(root,font=("Ariel",15),
            width=30)
e7.grid(row=8,column=1)


l8=tk.Label(root,text=" ",
          font=("Times New Roman",25)  )
l8.grid(row=15,column=1)

def store():
    name=e1.get()
    course=e2.get()
    sem=e3.get()
    contact=e4.get()
    em=e5.get()
    ad=e6.get()
    per=e7.get()
    if(e1.get()=="" and e2.get()=="" and e3.get()=="" and e4.get()=="" and e5.get()=="" and e6.get()=="" and e7.get()==""):
        l8["text"]="Please enter the above details"
    elif(e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or e6.get()=="" or e7.get()==""):
        l8["text"]="Please enter the above details"
    else:
        f=open("assign11.txt","+a")
        f.writelines(["\n NAME: ",name,"\n COURSE:",course,"\n SEMESTER: ",sem,"\n EMAIL ID: ",em,"\n ADDRESS: ",ad,"\n SSC PERCENTAGE: ",per])
        l8["text"]="Successfully Registered!"
        wb.open("https://www.tpolymumbai.in/")
        f.close()

b1=tk.Button(root,text="Submit",
             font=("Ariel",20),command=store)
b1.grid(row=12,column=1)
b2=tk.Button(root,text="Close",
             font=("Ariel",20),command=root.destroy)
b2.grid(row=14,column=1)

root.mainloop()

#ASSIGNMENT 12
from tkinter import *
import webbrowser as wb
def New_Travel():
    Window =Toplevel()
    canvas =Canvas(Window, height=300, width=500)
    canvas.pack()

    l5=Label(Window,text="Metro",foreground="black",font=("Calibri",25))
    l5.place(x=50,y=0)
    

    l6=Label(Window,text="Metro",foreground='blue',
             font=("Calibri",15))
    l6.place(x=30,y=120)
    e1=Entry(Window,font=("Calibri",15),width=30)
    e1.place(x=30,y=150)

    l7=Label(Window,text="Card Number",foreground='blue',
             font=("Calibri",15))
    l7.place(x=30,y=200)
    e2=Entry(Window,font=("Calibri",15),width=30)
    e2.place(x=30,y=250)

    l8=Label(Window,text="Amount",foreground='blue',
             font=("Calibri",15))
    l8.place(x=30,y=300)
    e3=Entry(Window,font=("Calibri",15),width=30)
    e3.place(x=30,y=350)

    l10=Label(Window,text="",font=("Calibri",15))
    l10.place(x=30,y=500)

    def storeRecharge():
        flag=1
        op=e1.get()
        num=e2.get()
        amount=e3.get()
        if(e1.get()=="" and e2.get()=="" and e3.get()=="" ):
            l10["text"]="Please enter the above details"
        elif(e1.get()=="" or e2.get()=="" or e3.get()=="" ):
            l10["text"]="Please enter the above details"
        else:
            f=open("PaytmData.txt","+a")
            f.writelines(["\n Metro: ",op,"\n Card number:",num,"\n Amount: ",amount])
            l8["text"]="Payment Successfull!"
            f.close()
        flag=0
        if resume.get()==1:
            flag=1
    rebutton=Button(Window,text="Proceed to Recharge",foreground="white",background="light blue",
                    font=("Calibri",20),command=storeRecharge)
    rebutton.place(x=30,y=450)

    l9=Label(Window,text="Browse Operator Plans",font=("Calibri",25))
    l9.place(x=30,y=550)


    
    def Mumbai():
        wb.open("https://www.mmmocl.co.in/card-reload.html")
    Mbutton=Button(Window,text="Mumbai Metro",foreground="white",background="purple",
                     font=("Ariel",20),command=Mumbai)
    Mbutton.place(x=30,y=600)

    def hyderabad():
        wb.open("https://www.ltmetro.com/")
    Hbutton=Button(Window,text="Hyderabad Metro",foreground="white",background="green",
                     font=("Ariel",20),command=hyderabad)
    Hbutton.place(x=300,y=600)

    lresume=Label(Window,text="Do you want to continue if yess press 1",
                  font=("Calibri",15))
    lresume.place(x=600,y=600)
    resume=Entry(Window,text="enter 1 to continue",font=("Calibri",15))
    resume.place(x=950,y=600)
#ASSIGNMENT 12
import webbrowser as wb
from tkinter import *
def New_Window():
    Window =Toplevel()
    canvas =Canvas(Window, height=300, width=500)
    canvas.pack()

    l5=Label(Window,text="Recharge or Pay Mobile Bill",foreground="black",font=("Calibri",25))
    l5.place(x=50,y=0)


    plan=Label(Window,text="Prepaid/Postpaid",foreground="blue",
                   font=("Calibri",15))
    plan.place(x=30,y=50) 
    plan1=Entry(Window,font=("Calibri",15))
    plan1.place(x=30,y=80)
    

    l6=Label(Window,text="Mobile Number",foreground='blue',
             font=("Calibri",15))
    l6.place(x=30,y=120)
    e1=Entry(Window,font=("Calibri",15),width=30)
    e1.place(x=30,y=150)

    l7=Label(Window,text="Operator",foreground='blue',
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
        mode=plan1.get()
        contact=e1.get()
        op=e2.get()
        amount=e3.get()
        if(e1.get()=="" and e2.get()=="" and e3.get()=="" and plan1.get==""):
            l10["text"]="Please enter the above details"
        elif(e1.get()=="" or e2.get()=="" or e3.get()=="" or plan1.get==""):
            l10["text"]="Please enter the above details"
        else:
            f=open("PaytmData.txt","+a")
            f.writelines(["\n Plan: ",mode,"\n Mobile No: ",contact,"\n Operator:",op,"\n Amount: ",amount])
            l8["text"]="Payment Successfull!"
            f.close()
        flag=0
        if resume.get()==1:
            flag=1
    rebutton=Button(Window,text="Proceed to Recharge",foreground="white",background="light blue",
                    font=("Calibri",20),command=storeRecharge)
    rebutton.place(x=30,y=450)

    l9=Label(Window,text="Check Out Operator Plans",font=("Calibri",25))
    l9.place(x=30,y=550)


    
    def airtel():
        wb.open("https://www.airtel.in/recharge-online")
    airbutton=Button(Window,text="Airtel",foreground="white",background="red",
                     font=("Ariel",20),command=airtel)
    airbutton.place(x=30,y=600)

    def jio():
        wb.open("https://www.jio.com/selfcare/plans/mobility/prepaid-plans-home/")
    jiobutton=Button(Window,text="Jio",foreground="white",background="blue",
                     font=("Ariel",20),command=jio)
    jiobutton.place(x=200,y=600)

    lresume=Label(Window,text="Do you want to continue if yess press 1",
                  font=("Calibri",15))
    lresume.place(x=500,y=600)
    resume=Entry(Window,text="enter 1 to continue",font=("Calibri",15))
    resume.place(x=900,y=600)





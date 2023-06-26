flag=1
while flag==1:
    print("------------WELCOME------------")
    print("\n 1. ADDITION \n 2.SUBTRACTION \n 3.MULTIPLICATION \n 4.DIVISION \n 5. REMAINDER \n 6. EXPONENT \n 7. FLOOR DIVISION")
    print()
    num1=int(input("Enter First Number"))
    num2=int(input("Enter Second Number"))
    choice=int(input("Enter Your Choice"))

    if choice==1:
         print("Addition Of",num1,"&",num2,"=",num1+num2)
    elif choice==2:
         print("Subtraction Of",num1,"&",num2,"=",num1-num2)
    elif choice==3:
        print("Multiplication Of",num1,"&",num2,"=",num1*num2)
    elif choice==4:
        print(num1,"Divide By",num2,"=",num1/num2)
    elif choice==5:
        print("Remainder after Dividing",num1,"by",num2,"=",num1%num2)
    elif choice==6:
        print(num1,"Raise to",num2,"=",num1**num2)
    elif choice==7:
        print("Floor Division:",num1//num2)
    else:
        print("Please Enter Correct Choice")
        flag=0
    print()
    resume=int(input("Do you want to continue? If yes enter 1 else press any number"))
    if(resume==1):
        flag=1
    else:
        print("Thank You")
        flag=0


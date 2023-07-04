'''1) Create a module consisting of class holding various data members and member functions.
(class can be on various file operations or mathematical operations or string operations)

2) Import the above module created and try to implement their member functions.

3) Also in the same file, create a user defined exception and implement it.'''




class CannotReadEmptyFileExcep(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class A:
    def func(self):
        flag=1
        while flag==1:
            print("-----------------WELCOME-----------------")
            print("\n 1. Open the file in Create mode \n 2. Open the file in Append mode \n 3. Open the file in Read mode \n 4. Open the file in Write mode")
            print()
            choice=int(input("Enter your Choice"))
            if choice==1:
                try:
                    src=open("source.txt","+x")
                except IOError:
                    print("This File Already Exists")
                ch1=int(input("Do you want to WRITE data to the file? If yes press 1 else press any number"))
                if(ch1==1):
                    src.writelines("Hello This is Source File In Create Mode\n")
                    print("Write Operation Sucessful!")

                ch2=int(input("Do you want to READ data from the file? If yes press 1 else any number"))
                if(ch1 != 1):
                    try:
                        raise CannotReadEmptyFileExcep("Cannot Read Data from Empty File!")
                    except CannotReadEmptyFileExcep as e:
                        print(e.args[0]) 
                elif(ch2==1):
                    src.seek(0)
                    print(src.read())
                
                    ch3=int(input("Do you want to COPY contents from this file to Another file ? If yes press 1"))#if exception is raised copy part is not executed
                    if(ch3==1):
                        des=open("Destination.txt","+a")  
                        src.seek(0)
                        data=src.readlines()
                        des.writelines(data)
                        print("Data Succesfully Copied!")
                print("----------------------END OF CHOICE 1------------------")
                

            elif choice==2:
                src=open("source.txt","+a")
                ch1=int(input("Do you want to WRITE data to the file? If yes press 1 else press any number"))
                if(ch1==1):
                    src.writelines("Hello This is Source File In Append Mode\n")
                    print("Write Operation Sucessful!")

                ch2=int(input("Do you want to READ data from the file? If yes press 1 else any number"))
                if(ch1 != 1):
                    try:
                        raise CannotReadEmptyFileExcep("Cannot Read Data from Empty File!")
                    except CannotReadEmptyFileExcep as e:
                        print(e.args[0]) 
                elif(ch2==1):
                    src.seek(0)
                    print(src.read())
                
                    ch3=int(input("Do you want to COPY contents from this file to Another file ? If yes press 1"))
                    if(ch3==1):
                        des=open("Destination.txt","+a")  
                        src.seek(0)
                        data=src.readlines()
                        des.writelines(data)
                        print("Data Succesfully Copied!")
                print("----------------------END OF CHOICE 2------------------")

            elif choice==3:
                src=open("source.txt","r")
                ch1=int(input("Do you want to WRITE data to the file? If yes press 1 else press any number"))
                if(ch1==1):
                    try:
                        src.writelines("Hello This is Source File In Read Mode\n")
                        print("Write Operation Sucessful!")
                    except IOError:
                        print(" You Cannot Write Data to a File in Read Mode  ")

                ch2=int(input("Do you want to READ data from the file? If yes press 1 else any number"))
                if(ch1 !=  1):
                    try:
                        raise CannotReadEmptyFileExcep("Cannot Read Data from Empty File!")
                    except CannotReadEmptyFileExcep as e:
                        print(e.args[0]) 
                elif(ch2==1):
                    src.seek(0)
                    print(src.read())
                
                    ch3=int(input("Do you want to COPY contents from this file to Another file ? If yes press 1"))
                    if(ch3==1):
                        des=open("Destination.txt","+a")  
                        src.seek(0)
                        data=src.readlines()
                        des.writelines(data)
                        print("Data Succesfully Copied!")
                print("----------------------END OF CHOICE 3-------------------")
        
            elif choice==4:
                src=open("source.txt","+w")
                ch1=int(input("Do you want to WRITE data to the file? If yes press 1 else press any number"))
                if(ch1==1):
                    src.writelines("Hello This is Source File In Write Mode\n")
                    print("Write Operation Sucessful!")

                ch2=int(input("Do you want to READ data from the file? If yes press 1 else any number"))
                if(ch1 != 1):
                    try:
                        raise CannotReadEmptyFileExcep("Cannot Read Data from Empty File!")
                    except CannotReadEmptyFileExcep as e:
                        print(e.args[0]) 
                elif(ch2==1):
                    src.seek(0)
                    print(src.read())
                
                    ch3=int(input("Do you want to COPY contents from this file to Another file ? If yes press 1"))
                    if(ch3==1):
                        des=open("Destination.txt","+a")  
                        src.seek(0)
                        data=src.readlines()
                        des.writelines(data)
                        print("Data Succesfully Copied!")
                print("----------------------END OF CHOICE 4------------------")
            else:
                print("PLEASE ENTER CORRECT CHOICE")
                flag=0
            print()
            resume=int(input("Do you want to continue? If yes enter 1 else press any number"))
            if(resume==1):
                flag=1
            else:
                print("Thank You")
                flag=0


        



        

ob=A()
ob.func()


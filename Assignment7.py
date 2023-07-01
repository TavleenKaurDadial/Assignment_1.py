'''1) Create a function with default parameter "file" storing the file path
2) Open the "file" in append mode
3) Use writelines() method to add your roll number, name, and class
4) Use readines() method to print your data in the prompt'''

def func(f="file"):
    try:
        file=open("Assign7.txt","+a")
        file.writelines("ROLL NO: 7 \n NAME: Tavleen Kaur \n CLASS: IF41")
        file.seek(0)
        print(file.read())
    except IOError:
        print("Exception is handled")
func()
print("------------------Continue Statement------------------")
i=1
while i<=10:
    if i==5:
        i+=1
        continue      # It returns the control to the beginning of the loop.
    print(i)
    i+=1
print()

print("------------Pass & For With Else Statement------------")
str="Tavleen"
for i in str:
    if i=="l":
       pass           # When we execute the pass statements then nothing happens.It is a null Operation.
    else:
        print(i)
else:
    print("It has Pass")  # when i reaches the last index then this statement is executed
print()


print("------------Break & While With Else Statement------------")
i=1                
while i<=10:
    if i==5:
        break
    else:
        print(i)
        i+=1
else:
    print("It has a break")        #if i=11 then print("it has a break") is executed


   
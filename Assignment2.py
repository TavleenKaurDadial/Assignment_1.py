print("-------------Arithmetic Operator----------------")
a=20
b=10
print("Addition of",a,"&",b,"=",a+b)
print("Subtraction of",a,"&",b,"=",a-b)
print("Multiplication of",a,"&",b,"=",a*b)
print("Division of",a,"&",b,"=",a/b)
print("Remainder of",a,"&",b,"=",a%b)
print("Floor Division=",a//b)
print("Exponent=",a**b)
print()

print("-------------Logical operator------------------")
a=True
b=False
print("And Operation :",a and b)
print("Or Operation :",a or b)
print("Not Operation :",not b)
print()


print("---------Comparison/Relational Operator---------")
x=30
y=20
print("Is",x,"greater than",y,"?",x>y)
print("Is",x,"less than",y,"?",x<y)
print("Is",x,"greater than equals",y,"?",x>=y)
print("Is",x,"less than equals",y,"?",x<=y)
print("Is",x,"equal to",y,"?",x==y)
print("Is",x,"not equals",y,"?",x!=y)
print()

print("--------------Assignment Operator--------------")
a=20
a+=1
print("+=",a)

a=20
a-=1
print("-=",a)

a=20
a*=2
print("*=",a)

a=20
a/=1
print("/=",a)

a=20
a//=2
print("//=",a)

a=20
a**=2
print("**=",a)

a=20
a%=2
print("%=",a)
print()


print("-------------Bitwise operator--------------")
p=10
q=2
print("Bitwise &",p&q)    
print("Bitwise |",p|q)  
print("Bitwise ^",p^q)
print("Bitwise >>",p>>q)    
print("Bitwise <<",p<<q) 
print()


print("-------------Identity Operator------------")
c=5
d=5
print("Is",c is d)
print("Is Not",c is not d)
print()


print("--------Special/Membership Operator----------")
str="Tavleen"
print("Is letter l present in str?",'l' in str)
print("Is letter p present in str?",'p' in str)
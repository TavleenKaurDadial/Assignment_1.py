'''1) Create 2 classes for single inheritance named respectively A(base class) and B(derived class)
2) Create 3 data members in class A: a(private), b(protected) and c(public) 
initialise their values in a parameterized constructor
3) Create a method known as display in both the classes, to display the values of a,b and c
4) While accessing the private member an exception should be raised and a \
      personalized message should be displayed and the exception should be
        handled properly so that the rest of the code can get executed'''


class PrivateMembAccessExcep(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class A :

   def __init__(self,a,b,c):
       self.__a=a
       self._b=b
       self.c=c
   def displayA(self):
        print("This is class A")
        print(self.__a)
        print(self._b)
        print(self.c)
       
class B(A):

    
    def displayB(self):
        print("This is class B")
        try:
             raise PrivateMembAccessExcep("Private Members of a class cannot be accessed in other class")
        except PrivateMembAccessExcep as e:
            print(e.args[0])
            print(self._b)
            print(self.c)

ob=B(10,20,30)
ob.displayA()
ob.displayB()

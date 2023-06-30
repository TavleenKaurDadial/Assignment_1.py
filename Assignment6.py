'''1)Create a function named ds with parameters roll_no and name.
2)Add those parameters in the following data structures:
list, tuple, sets and dictionaries
3) After adding values
change the values during runtime
4)Delete these data structures
'''


def ds(roll_no,name):
    print("Roll No:",roll_no,"\nName:",name)

ls=[0,"Tavleen"]       #list
ds(*ls)

t=(1,"Shraddha")       #tuple
ds(*t)

d={'roll_no':2, 'name':"random"}    #dictionary
ds(**d)

s={3,"xyzw"}            #set
ds(*s)

print()
'''xyz=ds("1","Tavleen")
print(xyz)'''
print("Changed values:")
ls[0]=1
ds(*ls)              #update list

#tuples are immutable

d1={"roll_no":3,"name":"random"}
d.update(d1)
ds(**d)                     #update roll_no dictionary
print()
print("Deleting All The Above Data Structures")
try:
    del ls
    ds(*ls)

    del t
    ds(*t)
    del d
    ds(**d)
    del s
    ds(*s)
except Exception:
    print("--------------All data structures are deleted------------")



    
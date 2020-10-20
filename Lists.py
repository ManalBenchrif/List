#Lists is similair to table
#list can contain any type of variable
#**********list of numbers*****************
liste=[1,2,3] # liste[0]=1,liste[1]=2,liste[2]=3
print(liste)
print("the value in position two =",liste[2]) #print 3,#Accessing an index which does not exist generates an exception (an error).

list1=[]
list1.append(4) # append() takes exactly one argument,its used to add a value into the list
list1.append(50)
print(list1)

#print out value of list using for
for i in liste:
    print(i)
print("end of liste")
#**********list of string*******************
listString=[]
listString.append("manal")
listString.append("theo")
listString.append("natali")
print(listString)

#Demonstration of set

print("Demonstration of set")

#data : heterogenious
#ordered : no
#indexed : no
#mutable : yes
#duplicates : no



data = {11,21,51,101,21,11}
data1 = {11,90,80,True,"hello"}

print("first set data a:",data)
print("length of data :",len(data))
print("data is heterogenious:",data1)
print("data is unorderd:",data1)
#print("data at index 2:",data1[2])
print("data with unique elements:",data)


print("set is mutable")
#insert element in set
data.add(211)
print("data after insertion:",data)

#remove element
data.remove(211)
print("data after removal:",data)


data.discard(201)
print("data after discard:",data)





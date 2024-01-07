#Demonstration of list

print("Demonstration of list")

#data : heterogeneous
#ordered : yes
#indexed : yes
#mutable : yes
#duplicates : yes


data = [11,21,51,101]
data1 = [11,90,80,True,"hello"]

print("data is heterogenious:",data1)
print("data is ordered:",data1)
print("data at index 2:",data1[2])
print("data with duplicate:",data)


print("list is mutable")
data.append(201)
print("data after append :",data)
data.pop()
print("data after pop :",data)

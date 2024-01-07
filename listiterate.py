#Demonstration of list

#data : heterogeneous
#ordered : yes
#indexed : yes
#mutable : yes
#duplicates : yes

Data = [11,21,51,101]
print("             ")

print("output using for")
for no in Data:
    print(no,end = " ")
print("             ")


print("output using for with index")
for i in range(0,len(Data)):
    print(Data[i],end = " ")
print("             ")


print("output using while with index")
i = 0
while(i < len(Data)):
    print(Data[i],end = " ")
    i+=1
print("            ")


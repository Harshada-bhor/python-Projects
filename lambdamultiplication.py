
##A programme which contains one lambda function which accept two parameter and
# return its multiplication.



multifunction = lambda A,B :A*B
print("How many element you want to store?")
Size = int(input())
Data = []
print("Please enter the data")
for i in range(0, Size, 1):
    value = int(input())
    Data.append(value)

Ans = multifunction(*Data)

print("Multiplication using lambda function :",Ans)



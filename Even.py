#Chake the given number is Even or not using normal function

def CheckEvenx(No):
    if(No%2 == 0):
        return True
    else:
        return False
#OR
def CheckEven(No):
    return (No%2 == 0)

Ret= CheckEvenx(12)

if(Ret == True):
    print("its even")
else:
    print("its odd")
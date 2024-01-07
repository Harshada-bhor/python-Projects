#Demonstrations of positonal & keywords arguments.
# positional arguments / keyword arguments
def Add1(No1,No2):
    
    print("value of No1 :",No1)
    print("value of No2 :",No2)
    return No1+No2

def Sub1(No1,No2):
    print("value of No1",No1)
    print("value of No2", No2)
    return No1-No2

def main():
    Ans = Add1(10,11)   #Positional arguments
    print("Addition is :",Ans)

    Ans = Sub1(No1 = 10, No2= 11)   #keyword arguments
    print("subtraction is :",Ans)

    Ans = Sub1(No2 = 10, No1= 11)   #keyword arguments
    print("subtraction is :",Ans)

if __name__ == "__main__":
    main()

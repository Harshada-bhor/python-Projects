# Inner functions types.
# function call inside function .

def Outer():    #100
    print("Inside Outer")

    def Inner():    #200
        print("Inside Inner")
    print(id(Inner))
    return Inner    #return 200



Ret= Outer()    #Ret=100()
print(type(Ret))
print(id(Ret))

Ret()   #200()

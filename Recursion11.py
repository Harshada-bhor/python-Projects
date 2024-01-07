#Demonstration of recursive function


def Fact(No):
    if(No<=0):
        return 1
    else:
        return(No*Fact(No-1))

def main():
    print("Enter a number")
    No = int(input())

    ret = Fact(No)
    print("Factorial is",ret)

if __name__== "__main__":
    main()
    
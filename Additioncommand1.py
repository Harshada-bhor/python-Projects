# Addition of Two numbers using cmdline Arguments.

from sys import *
def Addition(A,B):
    Ans = A+B
    return Ans

def main():
    print("welcome to : ",argv[0])
    if(len(argv) ==2):
        if(argv[1] == "__U"):
            print("use the application as : ")
            print("python name of application first number second number")
            exit()
        if(argv[1] == "__H"):
            print("Help = this application is used to perform addition of two numbers")
            exit()
    if(len(argv) !=3):
        print("invalid number of argumens")
        print("please use __U flag to get the usage")
        exit()
    Ret = Addition(int(argv[1]), int(argv[2]))
    print("Addition is : ",Ret)
    print("thank you for using this application")
    
if __name__ == "__main__":
    main()

    # for input cmd python Additioncommand1.py A B
    
    
     

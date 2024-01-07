#Addition of Two numbers using commandline Argument.

from sys import *
def Addition(A,B):

    Ans = A+B
    return Ans

def main():
    if(len(argv) !=3):
       print("invalid number of argumens")
       exit()
    Ret = Addition(int(argv[1]), int(argv[2]))
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()

    
    # for input cmd python Additioncommand.py A B


    
    
     

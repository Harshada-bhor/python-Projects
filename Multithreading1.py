## Python application which creates two thread evenfactor and oddfactor.
# both thread accept one parameter as a integer .Evenfactor thread display addition of
# evenfactor of given number. and Oddfactor thread display addition of Oddfactor
# of given number.
# After execution of both the thread gets completed main thread should display message
# as "Exit from main".


import time
import threading

def DisplayEvenfactor(No):
    sum = 0
    for i in range(1,int(No/2)+1,1):
        if(No%i == 0):
            if(i%2==0):
                sum=sum+i
    print("sum of even factor:",sum)


def DisplayOddfactor(No):
    sum=0
    for i in range(1,int(No/2)+1,1):
        if (No % i != 0):
            if(i%2 != 0):
                sum=sum+i
    print("sum of odd factor:",sum)



def main():
    print("demonstartion of parallel programming using multile processes")
    print("Enter a number")
    Number = int(input())
    
    p1= threading.Thread(target = DisplayEvenfactor,args = (Number,))
    p2= threading.Thread(target = DisplayOddfactor,args = (Number,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
   
    print("Exit from main")
if __name__ == "__main__":
    main()

    

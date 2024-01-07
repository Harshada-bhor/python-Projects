# Python application which creates two thread evenlist and oddlist.
# both thread accept one parameter as a integer .Evenlist thread add all even elements
# from input list and display addition of it.Oddlist thread add all odd elements
# # from input list and display addition of it.
# After execution of both the thread gets completed main thread should display message
# as "Exit from main".

import time
import threading

def DisplayEvenlist(Data):

    sum = 0
    for i in Data:
        if(i%2 == 0):
           sum=sum+i
    print("sum of even number:",sum)


def DisplayOddlist(Data):
    sum=0
    for i in Data:
        if (i % 2 != 0):
            sum=sum+i
    print("sum of odd number:",sum)



def main():
    print("demonstartion of parallel programming using multile processes")
    print("How many elements you want")
    Size=int(input())
    Data=[]
    print("Enter a Elements")
    for i in range(0,Size,1):
        value = int(input())
        Data.append(value)
    
    p1= threading.Thread(target = DisplayEvenlist,args = (Data,))
    p2= threading.Thread(target = DisplayOddlist,args = (Data,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
   
    print("Exit of main")
if __name__ == "__main__":
    main()

    

# Python application which creates three thread small, capital and digit.
# All thread accept one parameter as a string.small thread display no of small characters.
#capital thread display no of capital characters. digit thread display no of digits.
# Display id and name of each thread.
# After execution of both the thread gets completed main thread should display message
# as "Exit from main".


import time
import threading

def DisplaySmall(Data):

    for i in Data:
        if(i.islower()):
            print(i,end=",")
    print("")
    print("Name of the Thread:", threading.current_thread().name)
    print("Id of the Thread:", threading.get_ident())


def DisplayCapital(Data):
    for i in Data:
        if (i.isupper()):
            print(i, end=" ")
    print("")
    print("Name of the Thread:", threading.current_thread().name)
    print("Id of the Thread:", threading.get_ident())


def DisplayDigits(Data):
    print(len(Data))
    print("Name of the Thread:",threading.current_thread().name)
    print("Id of the Thread:",threading.get_ident())

def main():
    print("Enter a Element")
    Data=str(input())
    print("Name of the Thread:", threading.current_thread().name)
    print("Id of the Thread:", threading.get_ident())

    p1= threading.Thread(target = DisplaySmall,args = (Data,))
    p2= threading.Thread(target = DisplayCapital,args = (Data,))
    p3 = threading.Thread(target=DisplayDigits, args=(Data,))

    print("Small letters in Data:")
    p1.start()

    print("")

    print("Capital letters in Data:")
    p2.start()

    print("")

    print("Digits in Data:")
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Exit from main")
if __name__ == "__main__":
    main()

    

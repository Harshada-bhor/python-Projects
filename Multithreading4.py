## Python application which creates two thread as thread1 and thread2.
# thread1 Display 1 to 50 on screen. and thread2 display 50 to 1 on screen.
# After execution of both the thread gets completed main thread should display message
# as "Exit from main".

import time
import threading

def Thread1():
    for i in range(1,51,1):
        print( i,end=" ")

def Thread2():
    for i in range(50,0,-1):
       print(i,end=" ")


def main():
    print("demonstartion of parallel programming using multiple processes")

    
    p1= threading.Thread(target = Thread1,args = ())
    p2= threading.Thread(target = Thread2,args = ())

    print("Numbers in order:")
    p1.start()

    print("")

    print("Numbers in reverse order:")
    p2.start()
    
    p1.join()
    p2.join()

    print("")

    print("Exit from main")
if __name__ == "__main__":
    main()

    

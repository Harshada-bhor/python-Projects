# demonstartion of parallel programming using multiple processes
# Multithreading
# Python application which creates two thread even and odd. Even thread display first
# 10 even numbers and Odd thread display first 10 odd numbers.

import time
import threading

def DisplayEven(No):
    for i in range(1,No):
        if(i%2 == 0):
            print("even number:",i)


def DisplayOdd(No):
    for i in range(1,No):
        if(i%2 != 0):
            print("odd number:",i)


def main():
    print("demonstartion of parallel programming using multiple processes")
    Number = 20
    
    p1= threading.Thread(target = DisplayEven,args = (Number,))
    p2= threading.Thread(target = DisplayOdd,args = (Number,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
   
    print("End of main")

if __name__ == "__main__":

    start_time = time.process_time()

    main()

    end_time = time.process_time()
    print("Execution time is:",end_time-start_time)

    
    

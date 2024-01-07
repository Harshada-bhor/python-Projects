# To use Power of multicore processor we use pooling in python.
# Parallel Programming

import os
import multiprocessing

def Square(No):
    return (No*No)

def main():
    Data = [1,2,3,4,5]
    Result = []

    pobj = multiprocessing.Pool() # creating a pool object

    Result = pobj.map(Square, Data) # map list to target function

    print("Result afer square operation is ",Result)

if __name__ == "__main__":
    main()

    
    

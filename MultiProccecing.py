# demonstartion of serial programming
import time

def DisplayEven(No):
    for i in range(1,No):
        if(i%2 == 0):
            print("even number:",i)


def DisplayOdd(No):
    for i in range(1,No):
        if(i%2 != 0):
            print("odd number:",i)



def main():
    print("demonstartion of serial programming")
    DisplayEven(20)
    DisplayOdd(20)


if __name__ == "__main__":
    start_time = time.process_time()

    main()

    end_time = time.process_time()
    print("Execution time is:", end_time - start_time)

# OR 

if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print("Execution time is:", end_time - start_time)



    
    

# Demonstration of factors using while loop with different ranges.


def main():
    print("Enter number : ")
    No = int(input())
    i = 1

    print("factors are : ")
    while (i<= int(No/2)):
        if No % i == 0:
            print(i)
        i = i + 1
        
if __name__ == "__main__":
    main()
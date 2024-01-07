

#Application to display perticular pattern

def pattern1(n):
    i, j = 0, 0
    for i in range(1, n+1):
        print()
        for j in range(n, i-1, -1):
            print("*", end="\t")
    print(" ")

def pattern2(n):
    i, j = 0, 0
    for i in range(1, n+1):
        print()
        for j in range(1,i+1):
            print("*", end="\t")
    print(" ")

def pattern3(n):
    i, j = 0, 0
    for i in range(1, n+1):
        print()
        for j in range(1,(n-i)+1):
            print("*", end="\t")

def pattern4(n):
    i,j = 0,0
    for i in range (1,n+1):
        print()
        for j in range (1,n+1):
           print( j , end = "\t")


def main():
    print("Enter a number")
    n = int(input())
    pattern1(n)
    pattern2(n)
    pattern3(n)
    pattern4(n)


if __name__ == "__main__":
    main()


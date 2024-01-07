
# Application to find out first 10 even number


def main():
    print("Enter a number")
    No = int(input())

    for i in range(2,No*2+1,2):
        print(i , end = "  ")
#OR
    i=1
    while(i<=20):
        if i%2==0:
            print(i , end="  ")
        i=i+1

if __name__ == "__main__":
    main()
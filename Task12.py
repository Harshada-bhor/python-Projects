

#Application to display perticular pattern


def main():

    print("Enter a number")
    n = int(input())
   # i,j = 0,0
    for i in range (0,n):
        print()
        for j in range (i,i+5):
           print("*", end = "\t")

if __name__ == "__main__":
    main()

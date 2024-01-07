

#Application to display perticular pattern




def main():
    print("Enter a number")
    n = int(input())
   # i,j = 0,0
    for i in range (1,n+1):
        print()
        for j in range (1,i+1):
            print(j, end = "\t")
            

if __name__ == "__main__":
    main()

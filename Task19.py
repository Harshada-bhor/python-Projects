# Application to find sum of digits


def main():
    print("Enter a numbers")
    no = int(input())
    no= str(no)
    sum = 0
    for i in no:
        sum=sum+int(i)
    print("Sum is :",sum)
    return sum

if __name__== "__main__":
    main()
    
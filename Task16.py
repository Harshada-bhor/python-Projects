
##A Programme which accept N numbers from user and store it into list.
# return minimum from all elements from that list.


def main():
    print("Enter number of elements you want to enter:")
    Size = int(input())

    Data = []
    print("Please enter the data")
    for i in range(0,Size,1):
        value = int(input())
        Data.append(value)


    print("Data is :",Data)

    Ans =min(Data)
    print("Smallest number is",Ans)


if __name__ == "__main__":
    main()

#A Programme which accept N numbers from user and store it into list.
# return addition of all elements from that list.

def Add(values):
    sum = 0
    for no in values:
        sum = sum + no
    return sum

def main():
    print("Enter number of elements you want to enter:")
    Size = int(input())

    Data = []
    print("Please enter the data")
    for i in range(0,Size,1):
        value = int(input())
        Data.append(value)

    print("Data is :",Data)

    Ans = Add(Data)
    print("Addition is",Ans)


if __name__ == "__main__":
    main()
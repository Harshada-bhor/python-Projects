
#A Programme which accept N numbers from user and store it into list.
# Accept one another number from user and return frequency of that number from list.

def frequency(Data,X):
    count = 0
    for i in Data:
        if i == X:
            count += 1
    return count

def main():
    print("Enter number of elements you want to enter:")
    Size = int(input())

    Data = []
    print("Please enter the data")
    for i in range(0,Size,1):
        value = int(input())
        Data.append(value)
    print("Data is :",Data)

    print("Element to search")
    X = int(input())

    Ans = frequency(Data,X)
    print("Frequency is",Ans)

if __name__ == "__main__":
    main()
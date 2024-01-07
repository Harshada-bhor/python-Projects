
# Application to check whether number is positive or negative

def main():
    print("Enter a number")
    No = int(input())
    if No > 0:
        print("number is positive")
    elif No == 0:
        print("number is zero")
    else:
        print("number is negative")

if __name__ == "__main__":
    main()

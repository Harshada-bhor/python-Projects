
# A Programme which accept no from user and returns its factorial.

def main():
    print("Enter number : ")
    No = int(input())
    S = 1
    if No < 0:
        print("factorial does not exit")
    elif No == 0:
        print("the factorial of zero is 1")
    else:
        for i in range(1, No + 1):
            S = S * i
        print("the factorial of No is", S)
if __name__ == "__main__":
    main()
    
#Application of Addition of two numbers



def Add(No1,No2):
    Ans = No1 + No2
    return Ans

def main():
    print("Enter a first number")
    No1 = int(input())
    print("Enter a second number")
    No2 = int(input())

    Sum = Add(No1,No2)
    print("Addition is : ",Sum)

if __name__ == "__main__":
    main()

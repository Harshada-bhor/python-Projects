# Addition of two numbers. numbers are given from user. and the Addition function is
# in Marvellous Module.



import MarvellousModule
def main():
    print("Enter first number : ")
    no1 = int(input())
    print("Enter second number : ")
    no2 = int(input())

    Sum = MarvellousModule.Addition(no1,no2)
    print("Addition is : ",Sum)
if __name__ == "__main__":
    main()
    


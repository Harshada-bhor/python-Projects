
import ArithmaticModule


def main():
    print("Enter first number : ")
    a = int(input())
    print("Enter second number : ")
    b = int(input())

    Sum = ArithmaticModule.Add(a,b)
    print("Addition is : ",Sum)

    Subtraction = ArithmaticModule.Sub(a,b)
    print("Subtraction is : ", Subtraction)

    Multiplication = ArithmaticModule.Mult(a,b)
    print("Multiplication is : ", Multiplication)

    Division = ArithmaticModule.Div(a,b)
    print("Division is : ", Division)

    #OR
    ans1,ans2,ans3,ans4 = ArithmaticModule.Arithmatic(a,b)
    print("Addition is : ", ans1)
    print("Subtraction is : ", ans2)
    print("Multiplication is : ", ans3)
    print("Division is : ", ans4)


if __name__ == "__main__":
    main()


# demonstration of Types of Arguments.

def Area(Radius,PI = 3.14):
    Result = PI*Radius * Radius
    return Result

def main():
    Rvalue = 10.5
    PIvalue = 3.14

# positional arguments
    Ans = Area(Rvalue,PIvalue)
    print("Area of circle is :",Ans)

# keyword arguments
    Ans = Area(PI= PIvalue, Radius=Rvalue)
    print("Area of circle is :", Ans)

# positional & default argument
    Ans = Area(10.5)
    print("Area of circle is :", Ans)

#keyword & defalt arguments
    Ans = Area(Radius =10.5)
    print("Area of circle is :", Ans)

# keyword arguments
    Ans = Area(PI = 7.10, Radius=10.5)
    print("Area of circle is :", Ans)


if __name__ == "__main__":
    main()

# Addition of List of  more than two numbers.

def Addx(*values):
    sum = 0
    for no in values:
        sum = sum + no
    return sum

#OR
def Addx(*values):
    sum = 0
    for i in range(0,len(values)):
        sum = sum + values[i]
    return sum

def main():
    Ans = Addx(1,7,9,4,6,5)
    print("Addition is :",Ans)


if __name__ == "__main__":
    main()

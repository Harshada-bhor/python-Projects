# Application to find number is prime or not


print("Enter a number")
No = int(input())
if No > 1:
    for i in range(2, No):
        if (No % i) == 0:
            print("number is not a prime number")
            break
    else:
        print("number is a prime number")
else:
    print("number is a prime number")


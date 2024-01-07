# Object Oriented Programming
# A Programme which contains one class named as Demo.
# Demo class contains one class variable as Value.
# there are two instance methods of class as Fun and Gun which displays values of
# instance variable'
# Initialise instance variable in init method by accepting the values from user.



class Demo():
    value = 0

    def __init__(self,a,b):
        self.no1 = a
        self.no2 = b


     def Fun(self):
         print("first number is :", self.no1 )

    def Gun(self):
        print("Second number is :",self.no2)


def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()
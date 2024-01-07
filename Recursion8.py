#Demonstration of recursive function


def Display(No):
    if(No > 0):
        print("*" , end = " ")
        No = No - 1
        Display(No)

Display(5)

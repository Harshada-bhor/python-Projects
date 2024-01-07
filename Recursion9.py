#Demonstration of recursive function


def Display(No):

    if(No > 1):
        No = No - 1
        Display(No)
        print(No , end = " ")

Display(6)

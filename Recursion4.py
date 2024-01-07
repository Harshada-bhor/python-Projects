# Demonstration of Recursion Function



def Display(No):

    if(No > 0):
        No = No - 1
        Display(No)  # Recursive function call
        print(No)

Display(4)          # function call
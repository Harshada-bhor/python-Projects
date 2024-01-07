# Demonstration of Recursion Function

def Display(No):

    while(No > 0):
        print(No)
        No = No - 1

Display(4)          # function call

#OR

def Display(No):

    if(No > 0):
        print(No)
        No = No - 1
        Display(No)         # Recursive function call

Display(4)          # function call
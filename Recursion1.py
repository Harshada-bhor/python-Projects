# Demonstration of Recursion Function



def Display(No):
    Cnt = 0

    while(Cnt < No):
        print("Hello")
        Cnt = Cnt + 1

Display(4)

#OR

def Display(No):
    Cnt = 0

    if(Cnt < No):
        print("Hello")
        Cnt = Cnt + 1
        Display(No)

Display(4)
# Demonstration of Recursion Function

# 4
#  4 * 3 * 2 * 1 = 24

def Fact(No):
    if(No <= 0):
        return 1
    else:
        return (No * Fact(No-1))


Ret = Fact(4)          # function call

print("Result is :",Ret)
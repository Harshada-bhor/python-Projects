# Demonstration of Recursion Function

# 4
#  3 + 2 + 1 = 6

def Add(No):
    if(No <= 0):
        return 0
    else:
        return (No + Add(No-1))


Ret = Add(3)          # function call

print("Result is :",Ret)
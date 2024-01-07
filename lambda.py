# Demonstration of lambda function or unnamed function.

# normal function or named functions
def Add(No1,No2):
    return No1+No2

# lambda functions/unnamed function
# lambda parameter : body
Addfunction = lambda A,B :A+B

Ans1 = Add(10,11)
Ans2 = Addfunction(10,11)

print("Addition using normal function :",Ans1)
print("Addition using lambda function :",Ans2)


print("type of lambda function is:",type(Addfunction))

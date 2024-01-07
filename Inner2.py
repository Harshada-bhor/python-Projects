# Inner functions types.
# function call inside function .

def Demo():
    print("Inside Demo")

def Fun():
    print("Inside Fun")

def Hello(FPTR):
    print("Inside Hello")

    FPTR()

Hello(Demo)
Hello(Fun)

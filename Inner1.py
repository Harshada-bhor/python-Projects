# Inner functions types.
# function call inside function .

def Demo():
    print("Inside Demo")

def Hello():
    print("Inside Hello")

    Demo()

Hello()
Demo()

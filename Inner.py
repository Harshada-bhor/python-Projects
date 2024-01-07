# Inner functions type.
# functon call inside function .


def Hello():
    print("Inside Hello")

    def Demo():
        print("Inside Demo")
    Demo()

Hello()

def func():
    x = 1

    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


func()


def nonlocal_func():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


nonlocal_func()

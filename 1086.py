try:
    a="bbb"
    b="aaa"
    a=int(a)
    b=int(b)
    print(a/b)
except(ZeroDivisionError,ValueError):
    print("it's a invalid input")

def fib(n):
    a = 0
    b = 1
    print(a, b, end=" ")
    while a < n:
        c = a+b
        a = b
        b = c
        print(c, end=" ")


fib(10)

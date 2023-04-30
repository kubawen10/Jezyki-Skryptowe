from functools import lru_cache

def make_generator(f):
    x = 1
    def generator():
        nonlocal x
        while True:
            yield f(x)
            x+=1

    return generator

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def get_n(n, generator):
    for i, j in enumerate(generator()):
        print(j)
        if i >= n-1:
            print()
            break

fib_gen = make_generator(fibonacci)
#get_n(50, fib_gen)

range_gen = make_generator(lambda x: x)
get_n(5, range_gen)

mul2_gen = make_generator(lambda x: x*2)
get_n(5, mul2_gen)




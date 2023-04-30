from functools import lru_cache

def make_generator_mem(f):
    def generator():
        
        @lru_cache(None)
        def make_memoize_f(x):
            return f(x)

        x = 1
        while True:
            yield make_memoize_f(x)
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

fib_gen = make_generator_mem(fibonacci)
get_n(50, fib_gen)
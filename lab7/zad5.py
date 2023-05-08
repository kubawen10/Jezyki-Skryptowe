from functools import cache
from zad4 import make_generator, fibonacci
import time

@cache
def make_generator_mem(f):
    mem_f = cache(f)
    return make_generator(mem_f)

def get_n(n, function, description):
    print(f'{n} {description}')
    generator = make_generator_mem(function)
    for i, j in enumerate(generator()):
        if (i >= n-1):
            break

# it doesnt work in a way that fibonacci function memoizes recursively
# but rather running generator next time works faster
if __name__ == '__main__':
    start = time.time()
    get_n(35, fibonacci, "fibonacci numbers")
    print(f"first time: {time.time() - start} seconds")
    
    start = time.time()
    get_n(35, fibonacci, "fibonacci numbers second time")
    print(f"second time: {time.time() - start} seconds")
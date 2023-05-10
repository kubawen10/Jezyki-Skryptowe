def make_generator(f):
    def generator():
        n = 1
        while True:
            yield f(n)
            n+=1
    return generator

def fibonacci(x):
    if x<=1:
        return x
    else:
        return fibonacci(x-1) + fibonacci(x-2)

def get_n(n, function, description):
    print(f'{n} {description}')
    generator = make_generator(function)
    for i, j in enumerate(generator()):
        print(j)
        if (i >= n-1):
            print()
            break


if __name__ == '__main__':
    # takes time
    get_n(30, fibonacci, "fibonacci numbers")

    get_n(5, lambda x: x, "next numbers")

    get_n(5, lambda x: x*2, "numbers x*2")
    
    get_n(5, lambda x: 2**x, "numbers 2**x")

# doesnt work
# def get_n(n, function, description):
#     print(f'{n} {description}')
#     generator = make_generator(function)
#     for i, j in enumerate(generator()):
#         print(j, end=', ')
#         if (i >= n-1):
#             print()
#             break

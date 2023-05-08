import string
import random

class PasswordGenerator:
    def __init__(self, length: int, count: int, charset=string.ascii_letters + string.digits) -> None:
        self.length = length
        self.charset = charset
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.count:
            raise StopIteration
        
        self.index += 1
        return ''.join(random.choices(self.charset, k=self.length))
    


if __name__ == '__main__':
    print("First generator (length = 5, count = 3)")
    generator = PasswordGenerator(5,3)
    for password in generator:
        print(password)
    print("Trying to generate more in for loop: ")
    for password in generator:
        print(password)
    
    
    print("\nSecond generator (length = 5, count = 3)")
    generator = PasswordGenerator(5,3)
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print("Trying too many times: ")
    print(next(generator))
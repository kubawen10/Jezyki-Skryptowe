from typing import List

def acronym(words: List[str]):
    return ''.join([word[0] for word in words])

print(acronym(['Zaklad', 'Ubezpieczen', 'Spolecznych']))


def median(numbers: List[int]):
    sorted_numbers = numbers.sort()
    length = len(numbers)
    return sorted_numbers[length//2] if length % 2 == 1 else (sorted_numbers[length//2 - 1] + sorted_numbers[length//2]) / 2

print(median([1,1,19,2,3,4,4,5,1]))


def sqrt(x: int, epsilon: float):
    y = x / 2

    def inner_sqrt(y):
        return inner_sqrt((y + x / y)/2) if abs(y**2 - x) > epsilon else y
    
    return inner_sqrt(y)

print(sqrt(3, 0.01))


def make_alpha_dict(text: str):
    return {letter: [word for word in text.split() if letter in word] for letter in text.replace(' ', '')}

print(make_alpha_dict('on i ona i on'))


# for each sublist, for each element in either flatten(sublist)->(is list or tuple) or [sublist]->(is not list or tuple but we need to iterate over something so [sublist])
def flatten(elements):
    return [element for sublist in elements for element in (flatten(sublist) if isinstance(sublist, (list, tuple)) else [sublist])]

print(flatten([1, [2, 3], [[4, 5], 6]]))
print(flatten([1, 2]))
print(flatten([]))

from itertools import chain
from typing import Iterator
from rich import print
from sys import getsizeof
from string import ascii_letters

a: list[int] = [1, 2, 3]
b: list[int] = [111, 222]
c: tuple[int] = (10, 20)

my_chain: Iterator[int] = chain(a, b, c)
print(my_chain)

def test_drive_next():
    print(next(my_chain))
    print(next(my_chain))
    print(next(my_chain))
    print(next(my_chain))
    print(next(my_chain))
    print(next(my_chain))

def test_drive_combination():
    print(list(my_chain))
    print(a + b + list(c))

def test_drive_iterable():
    my_lists: list[list[int]] = [[1, 2, 3], [111, 222]]
    my_chain: Iterator[int] = chain.from_iterable(my_lists)
    print(list(my_chain))

def test_drive_size():
    print(ascii_letters)

    iter1: Iterator[str] = iter(ascii_letters)
    iter2: Iterator[int] = iter(range(1_000_000))
    my_chain: Iterator[str | int] = chain(iter1, iter2)
    print(getsizeof(iter1), 'bytes')
    print(getsizeof(iter2), 'bytes')
    print(getsizeof(my_chain), 'bytes')

    extracted: list[str | int] = list(my_chain)
    print(getsizeof(extracted), 'bytes')

if __name__ == "__main__":
    # test_drive()
    # test_drive_combination()
    # test_drive_iterable()
    test_drive_size()

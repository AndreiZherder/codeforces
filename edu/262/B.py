from math import floor
from os import path
from sys import stdin, stdout
from typing import Callable

if path.exists("input.txt"):
    stdin = open("input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def bsr(check: Callable[[float], bool], left: int = 0, right: int = 10 ** 18) -> int:
    """
    TTTTTFFF
         |
    """
    for i in range(100):
        mid = left + (right - left) / 2
        if check(mid):
            left = mid
        else:
            right = mid
    return mid


def solution():
    def check(mid: float) -> bool:
        return sum(int(length / mid) for length in lengths) >= k

    n, k = [int(num) for num in input().split()]
    lengths = []
    for i in range(n):
        lengths.append(int(input()))
    print(bsr(check, 0, max(lengths)))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

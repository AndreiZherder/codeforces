from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


# def input():
#     return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


import sys
from itertools import chain


def input_interactive(*args):
    print(' '.join(chain('?', map(str, args))))
    sys.stdout.flush()
    return input()


def print_interactive(*args):
    print(' '.join(chain('!', map(str, args))))
    sys.stdout.flush()


def solution():
    def ternary_search_left(left: int, right: int) -> int:
        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = left + 2 * (right - left) // 3
            s = int(input_interactive(mid1, mid2))
            if s == mid1 * mid2:
                left = mid2 + 1
            elif s == mid1 * (mid2 + 1):
                left = mid1 + 1
                right = mid2 - 1
            else:
                right = mid1 - 1
        return left
    print_interactive(ternary_search_left(1, 999))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

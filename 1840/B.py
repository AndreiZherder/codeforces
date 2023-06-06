import math
import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    # maximum quantity of numbers less than or equal to n which can be represented using k or less bits
    if k >= 30:
        print(n + 1)
    else:
        print(min(2 ** k, n + 1))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

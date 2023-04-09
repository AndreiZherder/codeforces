import sys
from math import gcd


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    a, b = [int(num) for num in input().split()]
    if gcd(a, b) == 1:
        print(1)
        print(a, b)
    else:
        print(2)
        if a < b:
            print(1, b - 1)
            print(a, b)
        else:
            print(a - 1, 1)
            print(a, b)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

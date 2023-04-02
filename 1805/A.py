import sys
from functools import reduce
from operator import xor

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    if n % 2 == 0:
        if reduce(xor, a) == 0:
            print(0)
        else:
            print(-1)
    else:
        y = reduce(xor, a)
        print(y)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

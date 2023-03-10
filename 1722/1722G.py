import sys
from functools import reduce
from operator import xor

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [1]
    for i in range(n - 1):
        a.append(a[-1] + i % 2 + 1)

    x = reduce(xor, a[:n - 2:2])
    y = reduce(xor, a[1:n - 2:2], 0)
    z1 = x ^ (2 ** 31 - 1)
    z2 = y ^ (2 ** 31 - 1)
    if n % 2 == 0:
        a[-1] = z2
        a[-2] = z1
    else:
        a[-1] = z1
        a[-2] = z2
    print(*a)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

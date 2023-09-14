from math import gcd
from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def sn(a1: int, an: int, n: int) -> int:
    return (a1 + an) * n // 2


def solution():
    n, x, y = [int(num) for num in input().split()]
    common = n // (x * y // gcd(x, y))
    m1 = n // x - common
    m2 = n // y - common
    print(sn(n, n - m1 + 1, m1) - sn(1, m2, m2))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

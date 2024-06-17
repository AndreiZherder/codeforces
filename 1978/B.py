from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
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
    n, a, b = [int(num) for num in input().split()]
    if b < a:
        print(n * a)
    else:
        m = min(b - a + 1, n)
        print(sn(b, b - m + 1, m) + (n - m) * a)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

from math import sqrt
from os import path
from sys import stdin, stdout


if path.exists("input.txt"):
    stdin = open("input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    c = float(input())
    left = 0
    right = 10 ** 10
    for i in range(100):
        mid = left + (right - left) / 2
        if mid * mid + sqrt(mid) >= c:
            right = mid
        else:
            left = mid
    print(left)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

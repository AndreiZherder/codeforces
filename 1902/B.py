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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    n, P, l, t = [int(num) for num in input().split()]
    x = ceil(n, 7)
    x2 = x // 2
    x1 = x % 2

    y2 = min(x2, ceil(P, 2 * t + l))
    points2 = y2 * (2 * t + l)
    if points2 >= P:
        print(n - y2)
        return
    P -= points2

    y1 = min(x1, ceil(P, t + l))
    points1 = y1 * (t + l)
    if points1 >= P:
        print(n - y2 - y1)
        return
    P -= points1

    y3 = ceil(P, l)
    print(n - y2 - y1 - y3)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

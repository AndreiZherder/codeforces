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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    n = int(input())
    k = [int(num) for num in input().split()]
    total = 10 ** 9
    x = []
    pref = 0
    for ki in k[:-1]:
        xi = ceil(total, ki)
        if xi * ki > total:
            x.append(xi)
            pref += xi
        else:
            x.append(xi + 1)
            pref += xi + 1
    x.append(total - pref)
    if sum(x) != total or x[-1] * k[-1] <= total:
        print(-1)
    else:
        print(*x)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
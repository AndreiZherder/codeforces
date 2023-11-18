from itertools import cycle, islice
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


def solution():
    n, m = [int(num) for num in input().split()]
    best = 10 ** 20
    for i in range(m):
        l, r = [int(num) for num in input().split()]
        best = min(best, r - l + 1)
    print(best)
    print(*islice(cycle(range(best)), n))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

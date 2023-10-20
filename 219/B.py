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
    p, d = [int(num) for num in input().split()]
    best = p
    for i in range(1, 19):
        x = p // (10 ** i) * (10 ** i) - 1
        if max(0, p - d) <= p // (10 ** i) * (10 ** i) - 1 <= p:
            best = max(best, x, key=lambda x: len(str(x)) - len(str(x).rstrip('9')))
    print(best)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

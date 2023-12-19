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
    n = int(input())
    a = sorted([(int(num), i) for i, num in enumerate(input().split())], reverse=True)
    b = sorted([(int(num), i) for i, num in enumerate(input().split())], reverse=True)
    c = sorted([(int(num), i) for i, num in enumerate(input().split())], reverse=True)
    best = 0
    for x, i in a[:3]:

        y, j = b[0]
        if j == i:
            y, j = b[1]
        z, k = c[0]
        if k == i or k == j:
            z, k = c[1]
            if k == i or k == j:
                z, k = c[2]

        best = max(best, x + y + z)

        z, k = c[0]
        if k == i:
            z, k = c[1]
        y, j = b[0]
        if j == i or j == k:
            y, j = b[1]
            if j == i or j == k:
                y, j = b[2]

        best = max(best, x + y + z)

    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

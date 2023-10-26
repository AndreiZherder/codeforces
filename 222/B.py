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
    n, m, k = [int(num) for num in input().split()]
    a = []
    rows = dict(enumerate(range(n)))
    cols = dict(enumerate(range(m)))
    for i in range(n):
        a.append([int(num) for num in input().split()])
    while k:
        s, x, y = input().split()
        x = int(x) - 1
        y = int(y) - 1
        if s == 'g':
            row = rows[x]
            col = cols[y]
            print(a[row][col])
        elif s == 'r':
            rows[x], rows[y] = rows[y], rows[x]
        else:
            cols[x], cols[y] = cols[y], cols[x]
        k -= 1


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

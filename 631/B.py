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
    a = [[0 for j in range(m)] for i in range(n)]
    operations = []
    while k:
        operations.append((int(num) for num in input().split()))
        k -= 1
    rows = set(range(n))
    cols = set(range(m))
    for op, i, color in reversed(operations):
        i -= 1
        if op == 1:
            if i in rows:
                for col in cols:
                    a[i][col] = color
                rows.remove(i)
        else:
            if i in cols:
                for row in rows:
                    a[row][i] = color
                cols.remove(i)
    for row in a:
        print(*row)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

from os import path
from sys import stdin, stdout

filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')
else:
    stdin = open('input.txt', 'r')
    stdout = open('output.txt', 'w')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    r1, c1, r2, c2 = [int(num) - 1 for num in input().split()]
    best = 10 ** 20
    j = min(c1, min(a[i] for i in range(min(r1, r2), max(r1, r2) + 1)))
    for i in range(r1, -1, -1):
        if a[i] < j:
            j = a[i]
        best = min(best, abs(i - r1) + abs(i - r2) + abs(j - c2))
    j = min(c1, min(a[i] for i in range(min(r1, r2), max(r1, r2) + 1)))
    for i in range(r1, n):
        if a[i] < j:
            j = a[i]
        best = min(best, abs(i - r1) + abs(i - r2) + abs(j - c2))
    print(best)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
from os import path
from sys import stdin, stdout
from types import GeneratorType

filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    best = 0
    total = 0
    mx = 0
    for i in range(k):
        if i < n:
            total += a[i]
            mx = max(mx, b[i])
        best = max(best, total + (k - i - 1) * mx)
    print(best)

def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

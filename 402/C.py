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
    n, p = [int(num) for num in input().split()]
    ans = []
    x = 0
    i = 1
    while i <= 2 * n + p:
        x += 1
        y = x + 1
        while i <= 2 * n + p and y <= n:
            ans.append((x, y))
            i += 1
            y += 1
    for x, y in ans:
        print(x, y)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

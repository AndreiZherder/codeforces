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
    x = [int(num) for num in input().split()]
    edges = []
    for i in range(m):
        edges.append([int(num) for num in input().split()])
    ans = 0
    for a, b, c in edges:
        ans = max(ans, (x[a - 1] + x[b - 1]) / c)
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

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
    delta = []
    total = 0
    for i in range(n):
        x, y = [int(num) for num in input().split()]
        total += x
        delta.append(x - y)
    delta.sort()
    overhead = total - m
    ans = 0
    while delta and overhead > 0:
        overhead -= delta.pop()
        ans += 1
    if overhead > 0:
        print(-1)
    else:
        print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

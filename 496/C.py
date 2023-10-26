from os import path
from sys import stdin, stdout
from typing import List

filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    def check(b: List[List[str]]) -> bool:
        for i in range(1, n):
            if ''.join(b[i]) < ''.join(b[i - 1]):
                return False
        return True

    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append(input())
    b = [[] for i in range(n)]
    ans = 0
    for j in range(m):
        for i in range(n):
            b[i].append(a[i][j])
        if not check(b):
            ans += 1
            for i in range(n):
                b[i].pop()
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
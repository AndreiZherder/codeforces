from itertools import count
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
    n, k = [int(num) for num in input().split()]
    ans = [[0 for j in range(n)] for i in range(n)]
    for j in range(n - 1, k - 2, -1):
        cur = n ** 2 - (n - 1 - j)
        for i in range(n):
            ans[i][j] = cur
            cur -= (n - k + 1)
    c = count(1)
    for i in range(n):
        for j in range(k - 1):
            ans[i][j] = next(c)
    print(sum(ans[i][k - 1] for i in range(n)))
    for row in ans:
        print(*row)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

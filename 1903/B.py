from functools import reduce
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
    a = []
    for i in range(n):
        a.append([int(num) for num in input().split()])
    ans = [2 ** 30 - 1 for i in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            ans[i] &= a[i][j]
            ans[j] &= a[i][j]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i][j] != ans[i] | ans[j]:
                print('NO')
                return
    print('YES')
    print(*ans)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append(input())
    ans = [['0' for j in range(n // k)] for i in range(n // k)]
    for i in range(0, n, k):
        for j in range(0, n, k):
            ans[i // k][j // k] = a[i][j]
    for row in ans:
        print(''.join(row))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

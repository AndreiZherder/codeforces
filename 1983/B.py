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
    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append([int(num) for num in input()])
    b = []
    for i in range(n):
        b.append([int(num) for num in input()])
    for i in range(n):
        if sum(a[i]) % 3 != sum(b[i]) % 3:
            print('NO')
            return
    for j in range(m):
        total_a = 0
        total_b = 0
        for i in range(n):
            total_a += a[i][j]
            total_b += b[i][j]
        if total_a % 3 != total_b % 3:
            print('NO')
            return
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

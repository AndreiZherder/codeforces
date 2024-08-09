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
        a.append([int(num) for num in input().split()])
    if n == m == 1:
        print(-1)
        return
    if m == 1:
        save = a[n - 1][0]
        for i in range(n - 1, 0, -1):
            a[i][0] = a[i - 1][0]
        a[0][0] = save
    else:
        for i in range(n):
            save = a[i][m - 1]
            for j in range(m - 1, 0, -1):
                a[i][j] = a[i][j - 1]
            a[i][0] = save
    for row in a:
        print(*row)




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

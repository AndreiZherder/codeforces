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
    n = int(input())
    ans = [['.' for j in range(2 * n)] for i in range(2 * n)]
    for i in range(2 * n):
        if i % 4 < 2:
            for j in range(2 * n):
                if j % 4 < 2:
                    ans[i][j] = '#'
        else:
            for j in range(2 * n):
                if j % 4 >= 2:
                    ans[i][j] = '#'
    for row in ans:
        print(''.join(row))



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

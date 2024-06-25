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
    x1, y1 = [int(num) for num in input().split()]
    x2, y2 = [int(num) for num in input().split()]
    if x1 > y1:
        if x2 > y2:
            print('YES')
        else:
            print('NO')
    else:
        if x2 < y2:
            print('YES')
        else:
            print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

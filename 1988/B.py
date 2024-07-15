from itertools import groupby
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
    s = input()
    ones = 0
    zeroes = 0
    for k, g in groupby(s):
        g = list(g)
        if k == '1':
            ones += len(g)
        else:
            zeroes += 1
    print('YES' if ones > zeroes else 'NO')



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

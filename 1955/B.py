from collections import Counter
from os import path
from random import getrandbits
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


RANDOM = getrandbits(32)


class Int(int):
    def __hash__(self):
        return super().__hash__() ^ RANDOM


def solution():
    n, c, d = [int(num) for num in input().split()]
    counter = Counter([Int(num) for num in input().split()])
    cur = min(counter)
    counter[Int(cur)] -= 1
    if counter[Int(cur)] == 0:
        del counter[Int(cur)]
    a = [[0 for j in range(n)] for i in range(n)]
    a[0][0] = cur

    for j in range(1, n):
        cur += d
        if Int(cur) not in counter:
            print('NO')
            return
        a[0][j] = cur
        counter[Int(cur)] -= 1
        if counter[Int(cur)] == 0:
            del counter[Int(cur)]

    for j in range(n):
        cur = a[0][j]
        for i in range(1, n):
            cur += c
            if Int(cur) not in counter:
                print('NO')
                return
            a[i][j] = cur
            counter[Int(cur)] -= 1
            if counter[Int(cur)] == 0:
                del counter[Int(cur)]

    for i in range(n):
        for j in range(1, n):
            if a[i][j] - a[i][j - 1] != d:
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

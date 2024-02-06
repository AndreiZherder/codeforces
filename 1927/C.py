from collections import Counter
from os import path
from random import getrandbits
from sys import stdin, stdout


filename = "../templates/input.txt"
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
    n, m, k = [int(num) for num in input().split()]
    a = {Int(num) for num in input().split()}
    b = {Int(num) for num in input().split()}
    c = Counter()
    for i in range(1, k + 1):
        x = Int(i)
        if x not in a and x not in b:
            print('NO')
            return
        if x in a:
            c['a'] += 1
        if x in b:
            c['b'] += 1
    if c['a'] < k // 2 or c['b'] < k // 2:
        print('NO')
    else:
        print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

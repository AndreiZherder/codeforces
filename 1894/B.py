from collections import Counter, defaultdict
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
    n = int(input())
    a = [Int(num) for num in input().split()]
    d = defaultdict(list)
    for i, ai in enumerate(a):
        d[ai].append(i)
    m = 0
    keys = []
    for ai in d:
        if len(d[ai]) >= 2:
            keys.append(ai)
            m += 1
    if m <= 1:
        print(-1)
        return
    else:
        cur = 2
        ans = [1 for i in range(n)]
        for j in range(m):
            v = d[keys[j]]
            ans[v[0]] = 1
            for i in range(1, len(v)):
                ans[v[i]] = cur
            if cur == 2:
                cur = 3
            else:
                cur = 2
        print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

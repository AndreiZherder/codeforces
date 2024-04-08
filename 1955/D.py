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
    n, m, k = [int(num) for num in input().split()]
    a = [Int(num) for num in input().split()]
    b = [Int(num) for num in input().split()]
    initial = Counter(b)
    target = initial.copy()
    counter = Counter()
    cur = 0
    ans = 0
    for i in range(m):
        counter[a[i]] += 1
        if a[i] in target:
            cur += 1
            target[a[i]] -= 1
            if target[a[i]] == 0:
                del target[a[i]]
    if cur >= k:
        ans += 1
    j = 0
    for i in range(m, n):
        if a[j] in initial:
            if counter[a[j]] <= initial[a[j]]:
                cur -= 1
                target[a[j]] += 1
        counter[a[j]] -= 1
        if counter[a[j]] == 0:
            del counter[a[j]]

        counter[a[i]] += 1
        if a[i] in target:
            cur += 1
            target[a[i]] -= 1
            if target[a[i]] == 0:
                del target[a[i]]
        if cur >= k:
            ans += 1
        j += 1
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

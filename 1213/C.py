from itertools import islice
from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    q = int(input())
    while q:
        n, m = [int(num) for num in input().split()]
        k = n // m
        cur = m
        seen = dict()
        while cur % 10 not in seen:
            seen[cur % 10] = 1
            cur += m
        l = len(seen)
        total = sum(seen)
        print(k // l * total + sum(islice(seen.keys(), k % l)))
        q -= 1


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

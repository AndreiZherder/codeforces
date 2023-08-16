from bisect import bisect_left
from itertools import accumulate
from os import path
from sys import stdin, stdout


if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, q = [int(num) for num in input().split()]
    pref = list(accumulate(sorted((int(num) for num in input().split()), reverse=True), initial=0))
    for i in range(q):
        x = int(input())
        cnt = bisect_left(pref, x)
        print(cnt if cnt < n + 1 else -1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

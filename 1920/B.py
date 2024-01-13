from itertools import accumulate
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
    n, k, x = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    a.sort(reverse=True)
    pref = list(accumulate(a, initial=0))
    best = -10 ** 20
    for i in range(k + 1):
        best = max(best, -(pref[min(n, i + x)] - pref[i]) + pref[n] - pref[min(n, i + x)])
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

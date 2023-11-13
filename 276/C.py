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
    n, q = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    a.sort(reverse=True)
    diff = [0 for i in range(n + 1)]
    while q:
        l, r = [int(num) - 1 for num in input().split()]
        diff[l] += 1
        diff[r + 1] -= 1
        q -= 1
    freq = list(accumulate(diff))
    freq.sort(reverse=True)
    ans = 0
    for ai, fi in zip(a, freq):
        ans += ai * fi
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

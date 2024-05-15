from bisect import bisect_right
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
    n, k, q = [int(num) for num in input().split()]
    a = [0] + [int(num) for num in input().split()]
    b = [0] + [int(num) for num in input().split()]
    ans = []
    while q:
        d = int(input())
        i = bisect_right(a, d)
        if i == len(a):
            ans.append(b[-1])
        else:
            ans.append((b[i - 1] + (d - a[i - 1]) * (b[i] - b[i - 1]) // (a[i] - a[i - 1])))
        q -= 1
    print(' '.join(map(str, ans)))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

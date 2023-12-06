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
    n, k, q = [int(num) for num in input().split()]
    m = 200000
    diff = [0 for i in range(m + 1)]
    for i in range(n):
        l, r = [int(num) - 1 for num in input().split()]
        diff[l] += 1
        diff[r + 1] -= 1
    a = list(accumulate(diff))
    pref = [0 for i in range(m + 1)]
    for i in range(1, m + 1):
        pref[i] = pref[i - 1] + (1 if a[i - 1] >= k else 0)
    while q:
        l, r = [int(num) - 1 for num in input().split()]
        print(pref[r + 1] - pref[l])
        q -= 1




def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

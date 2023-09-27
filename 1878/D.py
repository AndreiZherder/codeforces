from bisect import bisect_right
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
    n, k = [int(num) for num in input().split()]
    s = input()
    l = [int(num) - 1 for num in input().split()]
    r = [int(num) - 1 for num in input().split()]
    q = int(input())
    diff = [0 for i in range(n + 1)]
    xs = [int(num) - 1 for num in input().split()]
    for x in xs:
        i = bisect_right(l, x) - 1
        a = min(x, r[i] + l[i] - x)
        b = max(x, r[i] + l[i] - x)
        diff[a] += 1
        diff[b + 1] -= 1
    pref = list(accumulate(diff))
    ans = ['' for i in range(n)]
    for left, right in zip(l, r):
        j = bisect_right(l, left) - 1
        for i in range(left, right + 1):
            if pref[i] % 2 == 0:
                ans[i] = s[i]
            else:
                ans[i] = s[r[j] - (i - l[j])]
    print(''.join(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

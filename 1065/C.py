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
    hs = [int(num) for num in input().split()]
    diff = [0 for i in range(max(hs) + 1)]
    for h in hs:
        diff[0] += 1
        diff[h] -= 1
    a = list(accumulate(diff))
    a.pop()
    a.reverse()
    while len(a) >= 2:
        if a[-1] == a[-2]:
            a.pop()
        else:
            break
    a.pop()
    if not a:
        print(0)
        return
    ans = 0
    i = 0
    cur = 0
    while i < len(a):
        if cur + a[i] > k:
            ans += 1
            cur = a[i]
        else:
            cur += a[i]
        i += 1
    print(ans + 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

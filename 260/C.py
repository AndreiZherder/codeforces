from bisect import bisect_right
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
    n, x = [int(num) for num in input().split()]
    x -= 1
    a = [int(num) for num in input().split()]
    ans = a.copy()
    mn = min(a)
    minis = [i for i in range(n) if a[i] == mn]
    j = bisect_right(minis, x) - 1
    mini = minis[j]
    ans[mini] = 0
    k = a[mini]
    for i in range(n):
        if x > mini:
            if mini < i <= x:
                ans[i] -= 1
                ans[mini] += 1
        if x < mini:
            if i <= x or i > mini:
                ans[i] -= 1
                ans[mini] += 1
        if i != mini:
            ans[i] -= k
    ans[mini] += n * k
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

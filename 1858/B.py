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
    def cnt(x: int, y: int) -> int:
        if x == y:
            return 0
        if (x - y) % d == 0:
            add = -1
        else:
            add = 0
        return (x - y) // d + add


    n, m, d = [int(num) for num in input().split()]
    s = [1] + [int(num) for num in input().split()] + [n + 1]
    a = [0 for i in range(m + 2)]
    best = 0
    ans = []
    begin = 1
    if s[1] == 1:
        begin = 2
    for i in range(begin, m + 2):
        a[i] = cnt(s[i], s[i - 1])
    for i in range(begin, m + 1):
        cur = a[i] + a[i + 1] + 1 - cnt(s[i + 1], s[i - 1])
        if cur > best:
            best = cur
            ans = [s[i]]
        elif cur == best:
            ans.append(s[i])
    total = sum(a) + m - best
    if s[1] != 1:
        total += 1
    print(total, len(ans))






def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

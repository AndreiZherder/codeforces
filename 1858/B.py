from collections import deque
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
            return 1
        return (x - 1 - y) // d + 1


    n, m, d = [int(num) for num in input().split()]
    s = deque(int(num) for num in input().split())
    add = 0
    if s[0] == 1:
        s.popleft()
        m -= 1
        add = 1
    s.appendleft(1)
    s.append(n + 1)
    a = [0 for i in range(m + 2)]
    for i in range(m + 1):
        a[i] = cnt(s[i + 1], s[i])
    best = 0
    ans = 0
    for i in range(1, m + 1):
        cur = a[i - 1] + a[i] - cnt(s[i + 1], s[i - 1])
        if cur > best:
            best = cur
            ans = 1
        elif cur == best:
            ans += 1
    if best != 0:
        add = 0
    print(sum(a) - best, ans + add)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

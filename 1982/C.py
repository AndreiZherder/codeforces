from collections import deque
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
    n, l, r = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    q = deque()
    cur = 0
    ans = 0
    for i in range(n):
        cur += a[i]
        q.append(a[i])
        if cur <= r:
            if cur >= l:
                ans += 1
                q = deque()
                cur = 0
        else:
            while cur > r:
                cur -= q.popleft()
            if cur >= l:
                ans += 1
                q = deque()
                cur = 0
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

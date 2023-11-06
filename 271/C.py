from collections import deque
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
    if n < 3 * k:
        print(-1)
        return
    q = deque(range(n))
    ans = [0 for i in range(n)]
    m = n // k
    for i in range(k):
        for j in range(m - 1):
            ans[q.popleft()] = i + 1
        if len(q) == 1:
            ans[q.pop()] = i + 1
        else:
            last = q.pop()
            ans[q.pop()] = i + 1
            q.append(last)
    while q:
        ans[q.pop()] = i + 1
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

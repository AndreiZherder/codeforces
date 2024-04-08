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
    n, k = [int(num) for num in input().split()]
    q = deque([int(num) for num in input().split()])
    ans = 0
    step = 0
    while q:
        if len(q) == 1:
            if k >= q[0]:
                ans += 1
                q.popleft()
            else:
                break
        elif step == 0:
            if q[0] <= q[-1]:
                if k >= q[0] * 2 - 1:
                    ans += 1
                    q[-1] -= q[0] - 1
                    k -= q[0] * 2 - 1
                    q.popleft()
                    step = 1
                else:
                    break
            else:
                if k >= q[-1] * 2:
                    ans += 1
                    q[0] -= q[-1]
                    k -= q[-1] * 2
                    q.pop()
                else:
                    break
        else:
            if q[-1] <= q[0]:
                if k >= q[-1] * 2 - 1:
                    ans += 1
                    q[0] -= q[-1] - 1
                    k -= q[-1] * 2 - 1
                    q.pop()
                    step = 0
                else:
                    break
            else:
                if k >= q[0] * 2:
                    ans += 1
                    q[-1] -= q[0]
                    k -= q[0] * 2
                    q.popleft()
                else:
                    break
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

from collections import deque
from os import path
from sys import stdin, stdout
from typing import List

filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    def solve(start: int) -> List[int]:
        ans = [0 for i in range(n)]
        q = deque(range(1, n + 1))
        order = sorted(range(start, n - 1, 2), key=lambda i: nums[i])
        for i in order:
            ans[i] = q.pop()
        order = sorted(range(start - 1, n, 2), key=lambda i: nums[i], reverse=True)
        for i in order:
            ans[i] = q.popleft()
        if ans[0] == 0:
            ans[0] = q.pop()
        if ans[-1] == 0:
            ans[-1] = q.pop()
        return ans

    n = int(input())
    nums = [int(num) for num in input().split()]
    good = True
    for i in range(1, n - 1, 2):
        if nums[i] == 1 and (nums[i - 1] == n or nums[i + 1] == n):
            good = False
            break
    if good:
        print(*solve(1))
    else:
        print(*solve(2))



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

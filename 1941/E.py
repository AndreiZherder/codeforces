from collections import deque
from os import path
from sys import stdin, stdout
from typing import List

filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    def get_row_cost(nums: List[int]) -> int:
        dp = [0 for j in range(m)]
        q = deque()
        for j in range(m - 1, -1, -1):
            if not q:
                dp[j] = nums[j] + 1
                q.appendleft((dp[j], j))
            else:
                while q and q[-1][1] > j + d + 1:
                    q.pop()
                dp[j] = nums[j] + 1 + q[-1][0]
                while q and q[0][0] >= dp[j]:
                    q.popleft()
                q.appendleft((dp[j], j))
        return dp[0]


    n, m, k, d = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append([int(num) for num in input().split()])
    costs = []
    for i in range(n):
        costs.append(get_row_cost(a[i]))
    cur = sum(costs[:k])
    best = cur
    for i in range(k, n):
        cur += costs[i] - costs[i - k]
        best = min(best, cur)
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

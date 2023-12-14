from heapq import heappop, heappush
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
    x, k = [int(num) for num in input().split()]
    a = []
    b = [[(0, 0)] for i in range(k)]
    for i in range(k):
        l, *nums = [int(num) for num in input().split()]
        a.append([0] + nums + [-10 ** 20])
    pref = [list(accumulate(nums)) for nums in a]
    for i, nums in enumerate(pref):
        mx = 0
        best_mx = 0
        mn = 0
        for j in range(1, len(nums)):
            if nums[j] < 0 and nums[j - 1] >= 0:
                if mx > best_mx:
                    b[i].append((mn, mx))
                    best_mx = mx
                    mn = nums[j]
                    mx = nums[j]
            mx = max(mx, nums[j])
            mn = min(mn, nums[j])
    c = [[] for i in range(k)]
    for i in range(k):
        for (mn1, mx1), (mn2, mx2) in zip(b[i], b[i][1:]):
            c[i].append((mx1 - mn2, mx2 - mx1))
    h = []
    for i in range(k):
        c[i].reverse()
        if c[i]:
            heappush(h, (c[i].pop(), i))
    while h:
        (price, profit), i = heappop(h)
        if price > x:
            print(x)
            return
        else:
            x += profit
            if c[i]:
                heappush(h, (c[i].pop(), i))
    print(x)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

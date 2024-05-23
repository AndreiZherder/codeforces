from collections import defaultdict
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
    n = int(input())
    nums = [int(num) for num in input().split()]
    d12 = defaultdict(lambda: defaultdict(int))
    d23 = defaultdict(lambda: defaultdict(int))
    d13 = defaultdict(lambda: defaultdict(int))
    for i in range(n - 2):
        x1, x2, x3 = nums[i:i + 3]
        d12[(x1, x2)][x3] += 1
        d23[(x2, x3)][x1] += 1
        d13[(x1, x3)][x2] += 1
    ans = 0
    for x1, x2 in d12:
        total12 = sum(d12[(x1, x2)].values())
        for v in d12[(x1, x2)].values():
            ans += v * (total12 - v)
    for x2, x3 in d23:
        total23 = sum(d23[(x2, x3)].values())
        for v in d23[(x2, x3)].values():
            ans += v * (total23 - v)
    for x1, x3 in d13:
        total13 = sum(d13[(x1, x3)].values())
        for v in d13[(x1, x3)].values():
            ans += v * (total13 - v)
    print(ans // 2)







def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

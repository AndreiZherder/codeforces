from itertools import groupby
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
    n, k, x = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    groups = []
    for key, group in groupby(nums):
        groups.append(list(group))
    best = 0
    for i, group in enumerate(groups):
        cur = 0
        if group[0] == x and len(group) >= 2:
            l = i - 1
            r = i + 1
            cur += len(group)
            while l >= 0 and r < len(groups) and groups[l][0] == groups[r][0] and len(groups[l]) + len(groups[r]) >= 3:
                cur += len(groups[l]) + len(groups[r])
                l -= 1
                r += 1
            best = max(best, cur)
    print(best)



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

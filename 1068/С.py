from collections import defaultdict
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
    n, m = [int(num) for num in input().split()]
    ans = [[[i, i]] for i in range(n)]
    j = n
    pairs = []
    while m:
        pairs.append([int(num) - 1 for num in input().split()])
        m -= 1
    pairs.sort()
    for pair in pairs:
        for i in pair:
            if i != j:
                ans[i].append([i, j])
        j += 1
    for arr in ans:
        print(len(arr))
        for i, j in arr:
            print(i + 1, j + 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

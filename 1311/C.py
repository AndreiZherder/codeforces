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
    n, m = [int(num) for num in input().split()]
    s = input()
    p = [int(num) for num in input().split()]
    diff = [0 for i in range(n + 1)]
    for pi in p:
        diff[0] += 1
        diff[pi] -= 1
    diff[0] += 1
    diff[n] -= 1
    nums = list(accumulate(diff))
    ans = [0 for i in range(26)]
    for i in range(n):
        ans[ord(s[i]) - ord('a')] += nums[i]
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

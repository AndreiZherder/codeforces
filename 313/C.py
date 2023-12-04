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
    n = int(input())
    nums = sorted([int(num) for num in input().split()], reverse=True)
    pref = list(accumulate(nums, initial=0))
    i = 0
    ans = 0
    while 4 ** i <= n:
        ans += pref[4 ** i]
        i += 1
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

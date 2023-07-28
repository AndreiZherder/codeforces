from bisect import bisect_left, bisect_right
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    nums = sorted([int(num) for num in input().split()])
    k = int(input())
    for i in range(k):
        l, r = [int(num) for num in input().split()]
        print(bisect_right(nums, r) - bisect_left(nums, l))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

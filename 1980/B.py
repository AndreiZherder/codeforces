from bisect import bisect_left, bisect_right
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
    n, f, k = [int(num) for num in input().split()]
    f -= 1
    nums = [int(num) for num in input().split()]
    target = nums[f]
    nums.sort()
    i = bisect_left(nums, target)
    j = bisect_right(nums, target) - 1
    if k < n - j:
        print('NO')
    elif k < n - i:
        print('MAYBE')
    else:
        print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

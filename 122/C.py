from bisect import bisect_left, bisect_right
from itertools import product
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
    l, r = [int(num) for num in input().split()]
    nums = []
    for i in range(1, 11):
        nums.extend([int(''.join(t)) for t in product('47', repeat=i)])
    i = bisect_left(nums, l)
    j = bisect_right(nums, r)
    if i == j:
        m = r - l + 1
        ans = m * nums[i]
        print(ans)
        return
    m = nums[i] - l + 1
    ans = m * nums[i]
    for k in range(i + 1, j):
        m = nums[k] - nums[k - 1]
        ans += m * nums[k]
    m = r - nums[j - 1]
    ans += m * nums[j]
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

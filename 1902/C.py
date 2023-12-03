from math import gcd
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
    nums = sorted((int(num) for num in input().split()))

    if len(nums) == 1:
        print(1)
        return

    g = nums[1] - nums[0]
    for i in range(2, n):
        g = gcd(g, nums[i] - nums[i - 1])

    mx = nums[-1]
    for i in range(n - 1, 0, -1):
        if nums[i] - nums[i - 1] > g:
            nums.append(nums[i] - g)
            break
    else:
        nums.append(nums[0] - g)
    ans = 0
    for num in nums:
        ans += (mx - num) // g
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

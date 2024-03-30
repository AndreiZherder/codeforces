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
    n, x, y = [int(num) for num in input().split()]
    nums = sorted([int(num) for num in input().split()])
    ans = x - 2
    for num1, num2 in zip(nums, nums[1:]):
        if num2 - num1 == 2:
            ans += 1
    if (nums[0] - nums[-1]) % n == 2:
        ans += 1
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

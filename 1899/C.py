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
    nums = [int(num) for num in input().split()]
    best = -10 ** 20
    cur = 0
    prev = nums[0] % 2
    for num in nums:
        if num % 2 != prev:
            cur += num
            best = max(best, cur)
            cur = max(0, cur)
            prev ^= 1
        else:
            cur = num
            best = max(best, cur)
            cur = max(0, cur)
            prev = cur % 2
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

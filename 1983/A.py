from math import gcd
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


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def solution():
    n = int(input())
    # nums = [1 for i in range(n)]
    # for i in range(1, n + 1):
    #     for j in range(1, i + 1):
    #         if i % j == 0:
    #             nums[i - 1] = lcm(nums[i - 1], j)
    print(*range(1, n + 1))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

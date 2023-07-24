from math import sqrt
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, c = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    a = 4 * n
    b = 4 * sum(nums)
    c = sum(num ** 2 for num in nums) - c
    w = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(int(w))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

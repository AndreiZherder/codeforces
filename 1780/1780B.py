from itertools import accumulate
from math import gcd


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    a = list(accumulate(nums))
    best = 1
    for num in reversed(a[:n - 1]):
        best = max(best, gcd(a[-1], num))
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

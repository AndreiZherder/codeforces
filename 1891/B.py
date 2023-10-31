from collections import defaultdict
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


def least_set_bit(n: int) -> int:
    """
    least_set_bit(6) -> 2
    0110 -> 0010
    """
    return n & -n


def solution():
    n, q = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    xs = [int(num) for num in input().split()]
    d = defaultdict(set)
    for i, num in enumerate(nums):
        j = least_set_bit(num)
        while j:
            d[j].add(i)
            j >>= 1
    mx = 31
    for x in xs:
        y = pow(2, x)
        z = y >> 1
        if y in d:
            for i in d[y]:
                nums[i] += z
                d[z].add(i)
        for j in range(x, mx + 1):
            if 1 << j in d:
                del d[1 << j]
        mx = min(mx, x - 1)
    print(*nums)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

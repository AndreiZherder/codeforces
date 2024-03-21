from itertools import accumulate
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
    n, q = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    ones = [1 if num == 1 else 0 for num in nums]
    pref = list(accumulate(nums, initial=0))
    pref_ones = list(accumulate(ones, initial=0))
    while q:
        l, r = [int(num) - 1 for num in input().split()]
        if l == r:
            print('NO')
        else:
            total = pref[r + 1] - pref[l]
            total_ones = pref_ones[r + 1] - pref_ones[l]
            x = total_ones * 2 + (r - l + 1) - total_ones
            if x > total:
                print('NO')
            else:
                print('YES')
        q -= 1


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

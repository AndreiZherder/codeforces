from bisect import bisect_left
from itertools import accumulate
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, s = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    total = sum(nums)
    if total < s:
        print(-1)
        return
    target = total - s
    left_pref = list(accumulate(nums))
    right_pref = list(accumulate(reversed(nums)))
    left_total = 0
    best = 10 ** 20
    while left_total <= target:
        if left_total == 0:
            i = 0
        else:
            i = bisect_left(left_pref, left_total) + 1
        if target - left_total == 0:
            j = 0
        else:
            j = bisect_left(right_pref, target - left_total) + 1
        left_total += 1
        best = min(best, i + j)
    print(best)





def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

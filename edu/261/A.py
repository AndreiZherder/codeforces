from bisect import bisect_left
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    xs = [int(num) for num in input().split()]
    for x in xs:
        i = bisect_left(nums, x)
        if i != n and nums[i] == x:
            print('YES')
        else:
            print('NO')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

from functools import reduce
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    if all(nums[i] % 2 == nums[0] % 2 for i in range(n)):
        print('YES')
        return
    if all(nums[i] % 2 != nums[i + 1] % 2 for i in range(n - 1)):
        print('YES')
        return
    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

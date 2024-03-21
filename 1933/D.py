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
    n = int(input())
    nums = [int(num) for num in input().split()]
    ones = nums.count(1)
    if ones == 1:
        print('YES')
        return
    elif ones > 1:
        print('NO')
        return
    nums = sorted(num for num in nums if num != 1)
    x = nums[0]
    if nums.count(x) == 1 or any(num % x not in [0, x] for num in nums):
        print('YES')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

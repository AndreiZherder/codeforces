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
    total = sum(nums)
    if total % 3 == 0:
        print(0)
    elif n == 1:
        print(1)
    elif total % 3 == 2:
        print(1)
    elif any(num % 3 == 1 for num in nums):
        print(1)
    else:
        print(2)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

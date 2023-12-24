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


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    negative = 0
    for i, num in enumerate(nums):
        if num == 0:
            print(0)
            return
        elif num < 0:
            negative += 1
    if negative == 0:
        print(1)
        print(1, 0)
    elif negative % 2 == 0:
        print(1)
        print(1, 0)
    else:
        print(0)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

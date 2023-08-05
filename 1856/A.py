from os import path
from sys import stdin, stdout


if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    best = 0
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            best = max(best, nums[i])
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

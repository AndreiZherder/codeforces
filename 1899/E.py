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
    mini = 0
    mn = nums[0]
    for i in range(n):
        if nums[i] < mn:
            mn = nums[i]
            mini = i
    if nums[mini + 1:] == sorted(nums[mini + 1:]):
        print(mini)
    else:
        print(-1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

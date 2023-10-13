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
    s = sorted(nums)
    if s == nums:
        print(0)
        return
    i = 0
    j = n - 1
    while nums[i] == i + 1:
        i += 1
    while nums[j] == j + 1:
        j -= 1
    cnt = 0
    for k in range(i, j + 1):
        if nums[k] == k + 1:
            cnt += 1
    if cnt == 0:
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

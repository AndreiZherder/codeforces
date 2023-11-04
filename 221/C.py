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
    nums1 = [int(num) for num in input().split()]
    nums2 = sorted(nums1)
    cnt = 0
    for num1, num2 in zip(nums1, nums2):
        if num1 != num2:
            cnt += 1
    print('YES' if cnt <= 2 else 'NO')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

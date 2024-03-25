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
    prev = nums[n - 1]
    for i in range(n - 2, -1, -1):
        if prev < nums[i]:
            if nums[i] < 10:
                print('NO')
                return
            a = [int(c) for c in str(nums[i])]
            if prev < a[1]:
                print('NO')
                return
            elif a[1] < a[0]:
                print('NO')
                return
            else:
                prev = a[0]
        else:
            prev = nums[i]
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

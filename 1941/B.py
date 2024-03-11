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
    for i in range(n - 2):
        if nums[i + 1] < 2 * nums[i]:
            print('NO')
            return
        if nums[i + 2] < nums[i]:
            print('NO')
            return
        nums[i + 1] -= 2 * nums[i]
        nums[i + 2] -= nums[i]
    if nums[n - 2] != 0 or nums[n - 1] != 0:
        print('NO')
    else:
        print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

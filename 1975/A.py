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
    cnt = 0
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            cnt += 1
    if cnt == 0:
        print('YES')
        return
    if cnt == 1:
        if nums[-1] <= nums[0]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

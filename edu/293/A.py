from os import path
from sys import stdin, stdout


filename = '../../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, p = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    total = sum(nums)
    cnt = p // total * n
    p %= total
    if p == 0:
        print(1, cnt)
        return
    start = 0
    best = 10 ** 20
    nums *= 2
    n = len(nums)
    j = 0
    cur = 0
    for i in range(n):
        cur += nums[i]
        while cur >= p:
            if i - j + 1 < best:
                best = i - j + 1
                start = j
            cur -= nums[j]
            j += 1
    print(start + 1, cnt + best)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

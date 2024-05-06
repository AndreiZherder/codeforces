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
    nums = []
    _ = int(input())
    nums.extend([(int(num), 1) for num in input().split()])
    _ = int(input())
    nums.extend([(int(num), 2) for num in input().split()])
    _ = int(input())
    nums.extend([(int(num), 3) for num in input().split()])
    _ = int(input())
    nums.extend([(int(num), 4) for num in input().split()])
    nums.sort()
    n = len(nums)
    d = dict()
    best = 10 ** 20
    for i in range(n):
        x, cloth = nums[i]
        if cloth in d:
            del d[cloth]
        d[cloth] = x
        if len(d) == 4:
            diff = max(d.values()) - min(d.values())
            if diff < best:
                best = diff
                ans = [d[1], d[2], d[3], d[4]]
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

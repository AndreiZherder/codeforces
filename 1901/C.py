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
    nums.sort()
    cnt = 0
    while nums[-1] != nums[0]:
        cnt += 1
        for i in range(n):
            nums[i] = (nums[i] + nums[0]) // 2
    print(cnt)
    if cnt <= n:
        print(*[nums[0]] * cnt)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

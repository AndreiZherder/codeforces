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
    ans = 0
    cur = 1
    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            ans += cur * (cur + 1) // 2
            cur = 1
        else:
            cur += 1
    ans += cur * (cur + 1) // 2
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

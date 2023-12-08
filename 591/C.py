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
    best = 0
    cur = 0
    ans = nums[:]
    for i in range(1, n - 1):
        if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
            cur += 1
        else:
            if cur:
                best = max(best, (cur + 1) // 2)
                if cur % 2 == 0:
                    ans[i - cur:i - cur + cur // 2] = [nums[i - cur - 1]] * (cur // 2)
                    ans[i - cur + cur // 2:i] = [nums[i]] * (cur // 2)
                else:
                    ans[i - cur:i] = [nums[i]] * cur
                cur = 0
    if cur:
        best = max(best, (cur + 1) // 2)
        i = n - 1
        if cur % 2 == 0:
            ans[i - cur:i - cur + cur // 2] = [nums[i - cur - 1]] * (cur // 2)
            ans[i - cur + cur // 2:i] = [nums[i]] * (cur // 2)
        else:
            ans[i - cur:i] = [nums[i]] * cur
    print(best)
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

from os import path
from sys import stdin, stdout


if path.exists("../../templates/input.txt"):
    stdin = open("../../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    """
    FFFFTTTT
        |
    """
    def check(mid: int) -> bool:
        total = 0
        cnt = 1
        for num in nums:
            if num > mid:
                return False
            total += num
            if total > mid:
                cnt += 1
                total = num
        return cnt <= k

    left = 0
    right = sum(nums)
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(left)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

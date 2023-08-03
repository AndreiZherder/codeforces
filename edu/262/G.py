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
    k = int(input())
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    """
    TTTTFFFF
        |
    """
    def check(mid: int) -> bool:
        total = 0
        for num in nums:
            total += min(mid, num)
        return total // k >= mid

    left = 0
    right = sum(nums) // k
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(left - 1 if left - 1 >= 0 else 0)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

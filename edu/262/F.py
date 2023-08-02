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
    t = input()
    p = input()
    nums = [int(num) for num in input().split()]
    n = len(t)
    """
    TTTTFFFF
        |
    """
    def check(mid: int) -> bool:
        s = ''.join(t[i - 1] for i in (set(range(1, n + 1)) - set(nums[j] for j in range(mid))))
        i = -1
        for j in range(len(p)):
            i = s.find(p[j], i + 1)
            if i == -1:
                return False
        return True


    left = 0
    right = n
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(left - 1 if left - 1 >= 0 else 0)


def main():
    solution()


if __name__ == '__main__':
    main()

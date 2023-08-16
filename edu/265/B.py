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
    """
    FFFFTTTT
        |
    """
    def check(mid: int) -> bool:
        cnt = 0
        for i in range(1, n + 1):
            """
            TTTTFFFF
                |
            """
            left = 1
            right = n
            while left <= right:
                mid1 = left + (right - left) // 2
                if i * mid1 <= mid:
                    left = mid1 + 1
                else:
                    right = mid1 - 1
            cnt += left - 1
            if cnt >= k:
                break
        return cnt >= k

    left = 0
    right = n ** 2
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

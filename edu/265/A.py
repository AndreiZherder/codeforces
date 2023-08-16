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
    k += 1
    a = []
    for i in range(n):
        l, r = [int(num) for num in input().split()]
        a.append((l, r))
    """
    FFFFTTTT
        |
    """
    def check(mid: int) -> bool:
        cnt = 0
        for i in range(n):
            cnt += max(0, min(a[i][1], mid) - a[i][0] + 1)
        return cnt >= k

    left = -2 * 10 ** 9
    right = 2 * 10 ** 9
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

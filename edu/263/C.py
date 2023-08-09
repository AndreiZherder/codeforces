from bisect import bisect_left
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
    xs = [int(num) for num in input().split()]
    """
    TTTTFFFF
        |
    """
    def check(mid: int) -> bool:
        cur = xs[0]
        for i in range(k - 1):
            j = bisect_left(xs, cur + mid)
            if j == n:
                return False
            else:
                cur = xs[j]
        return True

    left = 0
    right = xs[-1] - xs[0]
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(left - 1)




def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

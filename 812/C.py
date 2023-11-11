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
    def bsr(left: int, right: int) -> int:
        """
        TTTTFFFF
            |
        """

        def check(mid: int) -> bool:
            b = sorted([a[i] + (i + 1) * mid for i in range(n)])
            return sum(b[:mid]) <= S

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left
    n, S = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    k = bsr(0, n) - 1
    if k == -1:
        print(0, 0)
        return
    b = sorted([a[i] + (i + 1) * k for i in range(n)])
    print(k, sum(b[:k]))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

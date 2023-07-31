from os import path
from sys import stdin, stdout


if path.exists("input.txt"):
    stdin = open("input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    def bsl(left: int, right: int) -> int:
        """
        FFFFFTTT
             |
        """

        def check(mid: int) -> bool:
            return (mid - min(x, y)) // x + (mid - min(x, y)) // y >= n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    n, x, y = [int(num) for num in input().split()]
    print(bsl(0, n * min(x, y)))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

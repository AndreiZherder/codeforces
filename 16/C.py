from math import gcd
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
            return mid * x <= a

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left
    a, b, x, y = [int(num) for num in input().split()]
    g = gcd(x, y)
    x //= g
    y //= g
    k = bsr(1, b // y) - 1
    if k == 0:
        print(0, 0)
        return
    b = k * y
    a = b * x // y
    print(a, b)





def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

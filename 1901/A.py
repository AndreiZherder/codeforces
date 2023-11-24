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
    def bsl(left: int, right: int) -> int:
        """
        TTTTFFFF
            |
        """

        def check(mid: int) -> bool:
            prev = 0
            for ai in a:
                if ai - prev > mid:
                    return False
                else:
                    prev = ai
            if (x - a[-1]) * 2 > mid:
                return False
            return True

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
    n, x = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    print(bsl(0, 2 * x + 1))



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

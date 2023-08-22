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
            y = min(c, m)
            if y < mid:
                return False
            return c + m + x - 2 * mid >= mid

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return max(0, left - 1)

    q = int(input())
    while q:
        c, m, x = [int(num) for num in input().split()]
        print(bsr(0, m + c + x))
        q -= 1



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

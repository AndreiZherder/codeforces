from collections import Counter
from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
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
        FFFFTTTT
            |
        """

        def check(mid: int) -> bool:
            c = [0 for i in range(20)]
            for i in range(mid):
                for bit in range(20):
                    if nums[i] & 1 << bit:
                        c[bit] += 1

            prev = 0
            for bit in range(20):
                if c[bit]:
                    prev |= 1 << bit

            for i in range(mid, n):
                for bit in range(20):
                    if nums[i] & 1 << bit:
                        c[bit] += 1
                j = i - mid
                for bit in range(20):
                    if nums[j] & 1 << bit:
                        c[bit] -= 1

                cur = 0
                for bit in range(20):
                    if c[bit]:
                        cur |= 1 << bit
                if cur != prev:
                    return False
            return True


        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    n = int(input())
    nums = [int(num) for num in input().split()]
    print(bsl(1, n))



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

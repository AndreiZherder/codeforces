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
        FFFFTTTT
            |
        """

        def check(mid: int) -> bool:
            cur_left = 0
            cur_right = 0
            for l, r in segments:
                if l - cur_right > mid or cur_left - r > mid:
                    return False
                else:
                    cur_left = max(cur_left - mid, l)
                    cur_right = min(cur_right + mid, r)
            return True


        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


    n = int(input())
    segments = []
    for i in range(n):
        segments.append([int(num) for num in input().split()])
    print(bsl(0, 10 ** 9))



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

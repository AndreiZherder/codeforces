from os import path
from sys import stdin, stdout


if path.exists("input.txt"):
    stdin = open("input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    w, h, n = [int(num) for num in input().split()]
    left = 1
    right = 10 ** 18 + 1
    while left <= right:
        mid = left + (right - left) // 2
        if mid // w == 0 or mid // h == 0:
            left = mid + 1
        else:
            x1 = mid // w
            y1 = (n + x1 - 1) // x1
            y2 = mid // h
            x2 = (n + y2 - 1) // y2
            if y1 * h <= mid or x2 * w <= mid:
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

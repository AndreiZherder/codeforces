from math import sqrt
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
    px, py = [int(num) for num in input().split()]
    ax, ay = [int(num) for num in input().split()]
    bx, by = [int(num) for num in input().split()]
    r1 = sqrt((ax - px) ** 2 + (ay - py) ** 2)
    r2 = sqrt((ax - 0) ** 2 + (ay - 0) ** 2)
    r3 = sqrt((bx - px) ** 2 + (by - py) ** 2)
    r4 = sqrt((bx - 0) ** 2 + (by - 0) ** 2)
    r5 = sqrt((ax - bx) ** 2 + (ay - by) ** 2)
    ans1 = min(max(r1, r2), max(r3, r4))
    # ans2 = sqrt((ax - bx) ** 2 + (ay - by) ** 2) / 2
    if r2 < r4:
        t1 = r2
    else:
        t1 = r4
    if r1 < r3:
        t2 = r1
    else:
        t2 = r3



    left = 0
    right = 10 ** 9
    for i in range(100):
        mid = (left + right) / 2
        if t1 <= mid and t2 <= mid and r5 <= 2 * mid:
            right = mid
        else:
            left = mid
    print(min(ans1, mid))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

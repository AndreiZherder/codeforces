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
    x1, y1 = [int(num) for num in input().split()]
    x2, y2 = [int(num) for num in input().split()]
    if x2 < x1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    n = int(input())
    lines = []
    for i in range(n):
        lines.append([int(num) for num in input().split()])
    ans = 0
    for a, b, c in lines:
        if b == 0:
            if x1 < -c / a < x2:
                ans += 1
        elif (y1 < (-c - a * x1) / b and (-c - a * x2) / b < y2) or ((-c - a * x1) / b < y1 and y2 < (-c - a * x2) / b):
            ans += 1
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

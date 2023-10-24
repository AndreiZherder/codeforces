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
    n, A = [int(num) for num in input().split()]
    d = [int(num) for num in input().split()]
    s = sum(d)
    ans = [0 for i in range(n)]
    dn = A - n
    ds = s - A
    for i, di in enumerate(d):
        y1 = max(0, di - dn - 1)
        y2 = max(0, di - ds - 1)
        ans[i] = min(di, y1 + y2)
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

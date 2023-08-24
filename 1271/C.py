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
    n, sx, sy = [int(num) for num in input().split()]
    t, b, l, r = 0, 0, 0, 0
    for i in range(n):
        x, y = [int(num) for num in input().split()]
        if x - sx > 0:
            r += 1
        elif x - sx < 0:
            l += 1
        if y - sy > 0:
            t += 1
        elif y - sy < 0:
            b += 1
    m = max(t, b, l, r)
    print(m)
    if t == m:
        print(sx, sy + 1)
    elif b == m:
        print(sx, sy - 1)
    elif r == m:
        print(sx + 1, sy)
    else:
        print(sx - 1, sy)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

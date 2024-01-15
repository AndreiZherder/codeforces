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
    xs = []
    ys = []
    for i in range(4):
        x, y = [int(num) for num in input().split()]
        xs.append(x)
        ys.append(y)
    xs.sort()
    ys.sort()
    print((xs[-1] - xs[0]) * (ys[-1] - ys[0]))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

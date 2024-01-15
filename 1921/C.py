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
    n, f, a, b = [int(num) for num in input().split()]
    m = [int(num) for num in input().split()]
    pos = 0
    for mi in m:
        cost = (mi - pos) * a
        if f - min(cost, b) <= 0:
            print('NO')
            return
        else:
            f -= min(cost, b)
            pos = mi
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

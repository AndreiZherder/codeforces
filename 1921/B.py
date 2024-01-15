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
    n = int(input())
    s = input()
    f = input()
    a = 0
    b = 0
    for c1, c2 in zip(s, f):
        if c1 == '1' and c2 == '0':
            a += 1
        if c1 == '0' and c2 == '1':
            b += 1
    x = min(a, b)
    y = max(a, b) - x
    print(x + y)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

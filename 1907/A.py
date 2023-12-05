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
    s = input()
    rows = 'abcdefgh'
    cols = '12345678'
    r = s[0]
    c = s[1]
    for row in rows:
        if row != r:
            print(row + c)
    for col in cols:
        if col != c:
            print(r + col)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

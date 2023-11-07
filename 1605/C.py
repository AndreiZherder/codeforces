from collections import Counter
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
    if 'aa' in s:
        print(2)
    elif 'aba' in s or 'aca' in s:
        print(3)
    elif 'abca' in s or 'acba' in s:
        print(4)
    elif 'abbacca' in s or 'accabba' in s:
        print(7)
    else:
        print(-1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

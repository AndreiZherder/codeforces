from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
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
    if any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789' for c in s):
        print('NO')
        return
    prev = s[0]
    for c in s[1:]:
        if c.isdigit() and prev.isalpha():
            print('NO')
            return
        prev = c
    prev = '0'
    for c in s:
        if c.isdigit():
            if c < prev:
                print('NO')
                return
            prev = c
    prev = 'a'
    for c in s:
        if c.isalpha():
            if c < prev:
                print('NO')
                return
            prev = c
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

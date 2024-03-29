from os import path
from sys import stdin, stdout

if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    s = input()
    n = len(s)
    if s == '()':
        print('NO')
        return
    if '((' in s or '))' in s:
        print('YES')
        print('()' * n)
    else:
        print('YES')
        print('(' * n + ')' * n)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

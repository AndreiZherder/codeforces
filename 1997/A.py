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
    s = input()
    n = len(s)
    for i in range(1, n):
        if s[i] == s[i - 1]:
            if s[i] != 'a':
                print(s[:i] + 'a' + s[i:])
                return
            else:
                print(s[:i] + 'b' + s[i:])
                return
    if s[-1] != 'a':
        print(s + 'a')
    else:
        print(s + 'b')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

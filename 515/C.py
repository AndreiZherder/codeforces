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
    d = {
        '0': '',
        '1': '',
        '2': '2',
        '3': '3',
        '4': '322',
        '5': '5',
        '6': '53',
        '7': '7',
        '8': '7222',
        '9': '7332'
         }
    n = int(input())
    s = input()
    ans = []
    for c in s:
        ans.extend(list(d[c]))
    print(''.join(sorted(ans, reverse=True)))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

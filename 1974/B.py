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
    r = sorted(set(s))
    m = len(r)
    d = dict()
    for i, c in enumerate(r):
        if i <= m // 2:
            d[c] = r[m - 1 - i]
            d[r[m - 1 - i]] = c
        else:
            break
    print(''.join(d[c] for c in s))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

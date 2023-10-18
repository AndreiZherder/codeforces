import string
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
    s = Counter(input())
    t = Counter(input())
    ans = [0, 0]
    for c in string.ascii_lowercase:
        x = min(s[c], t[c])
        y = min(s[c.upper()], t[c.upper()])
        ans[0] += x + y
        s[c] -= x
        t[c] -= x
        s[c.upper()] -= y
        t[c.upper()] -= y
        x = min(s[c], t[c.upper()])
        y = min(s[c.upper()], t[c])
        ans[1] += x + y
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

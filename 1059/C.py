from collections import Counter, defaultdict
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
    a = list(range(1, n + 1))
    ans = []
    while len(a) > 3:
        ans.extend([a[0]] * len(a[::2]))
        a = a[1::2]
    if len(a) == 1:
        ans.append(a[0])
    elif len(a) == 2:
        ans.append(a[0])
        ans.append(a[1])
    elif len(a) == 3:
        ans.append(a[0])
        ans.append(a[0])
        ans.append(a[2])
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

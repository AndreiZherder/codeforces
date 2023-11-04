from collections import Counter, defaultdict
from itertools import chain
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
    n = len(s)
    k = int(input())
    if k >= n:
        print(0)
        print()
        return
    d = defaultdict(list)
    for i, c in enumerate(s):
        d[c].append(i)
    for c in sorted(d, key=lambda c: len(d[c])):
        if k >= len(d[c]):
            k -= len(d[c])
            del d[c]
        else:
            d[c] = d[c][:len(d[c]) - k]
            break
    print(len(d))
    print(''.join(s[i] for i in sorted(chain.from_iterable(d.values()))))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

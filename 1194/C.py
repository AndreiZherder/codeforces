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
    s = input()
    t = input()
    p = Counter(input())
    n = len(s)
    m = len(t)
    if n > m:
        print('NO')
        return
    s = s + '#'
    i = 0
    j = 0
    while j < m:
        if s[i] == t[j]:
            i += 1
            j += 1
        elif p[t[j]] > 0:
            p[t[j]] -= 1
            j += 1
        else:
            print('NO')
            return
    if i == n:
        print('YES')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

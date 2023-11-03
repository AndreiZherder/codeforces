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
    _ = int(input())
    words = input().split()
    ans = 0
    d = [Counter() for i in range(6)]
    for word in words:
        d[len(word)][sum(int(c) for c in word)] += 1
    for word in words:
        n = len(word)
        for m in range(n, 0, -2):
            x = sum(int(c) for c in word[:(n + m) // 2])
            y = sum(int(c) for c in word[(n + m) // 2:])
            if x - y in d[m]:
                ans += d[m][x - y]
        for m in range(n - 2, 0, -2):
            x = sum(int(c) for c in word[::-1][:(n + m) // 2])
            y = sum(int(c) for c in word[::-1][(n + m) // 2:])
            if x - y in d[m]:
                ans += d[m][x - y]
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

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
    n = len(s)
    best = max(Counter(s).values())
    for i in range(10):
        for j in range(10):
            if j != i:
                cur = 0
                pos = -1
                while True:
                    pos = s.find(str(i), pos + 1)
                    if pos == -1:
                        break
                    pos = s.find(str(j), pos + 1)
                    if pos == -1:
                        break
                    cur += 2
                best = max(best, cur)
    print(n - best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

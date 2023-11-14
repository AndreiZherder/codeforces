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
    k = int(input())
    s = [int(num) for num in input()]
    acc = 0
    d = defaultdict(int)
    ans = 0
    d[0] = 1
    for num in s:
        acc += num
        ans += d[acc - k]
        d[acc] += 1
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

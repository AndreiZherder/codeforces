from collections import Counter
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    words = Counter()
    for i in range(n):
        words[input()] += 1
    ans = 0
    for (x1, y1), v1 in words.items():
        for (x2, y2), v2 in words.items():
            if x1 == x2 and y1 != y2:
                ans += v1 * v2
            if x1 != x2 and y1 == y2:
                ans += v1 * v2
    print(ans // 2)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

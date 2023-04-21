import string
import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    s = input()
    best = 10 ** 20
    for c in string.ascii_lowercase:
        parts = [part for part in s.split(c) if part]
        cur = 0
        for part in parts:
            cur = max(cur, len(part).bit_length())
        best = min(best, cur)
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

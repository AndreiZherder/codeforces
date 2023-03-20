import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    s = input()
    d = defaultdict(list)
    for i, c in enumerate(s):
        d[c].append(i)
    for i, c in enumerate(s):
        parity = i % 2
        if any(j % 2 != parity for j in d[c]):
            print('NO')
            return
        del d[c]
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

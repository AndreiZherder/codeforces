import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    words = input().split()

    if n == 1:
        print('YES')
        return

    d = defaultdict(list)
    for word in words:
        if len(word) == n // 2:
            d[n // 2].append(word)
        if len(word) == n // 2 + 1:
            d[n // 2 + 1].append(word)

    if n % 2 == 0:
        if d[n // 2][0] == d[n // 2][1][::-1]:
            print('YES')
            return
    else:
        if d[n // 2][0] == d[n // 2][1][::-1] and d[n // 2 + 1][0] == d[n // 2 + 1][1][::-1]:
            print('YES')
            return

    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

import sys
from collections import Counter

input = sys.stdin.readline


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, k = (int(num) for num in input().split())
    cnt = Counter()
    for i in range(n):
        l, r = (int(num) for num in input().split())
        if l <= k <= r:
            for j in range(l, r + 1):
                cnt[j] += 1

    if not cnt:
        print('NO')
        return

    if len(cnt) == 1:
        print('YES')
        return

    freqs = list(sorted(cnt.items(), key=lambda item: (-item[1], item[0])))
    if freqs[0][1] == freqs[1][1]:
        print('NO')
        return

    if freqs[0][0] == k:
        print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

from bisect import bisect_right
from collections import Counter, defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    s = input()
    m = int(input())
    l = input()
    r = input()
    db = defaultdict(list)
    for i, num in enumerate(s):
        db[int(num)].append(i)
    low = [int(l[i]) for i in range(m)]
    high = [int(r[i]) for i in range(m)]
    cur = low.copy()
    while cur[0] <= high[0]:
        pos = -1
        for i in range(m):
            if cur[i] not in db:
                print('YES')
                return
            index = bisect_right(db[cur[i]], pos)
            if index == len(db[cur[i]]):
                print('YES')
                return
            pos = db[cur[i]][index]
        i = m - 1
        cur[i] += 1
        while i >= 1 and cur[i] > high[i]:
            cur[i] = low[i]
            i -= 1
            cur[i] += 1
    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

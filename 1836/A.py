from collections import Counter
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    cnt = Counter(a)
    if 0 not in cnt:
        print('NO')
        return
    mx = max(cnt)
    for i in range(1, mx + 1):
        if i not in cnt:
            print('NO')
            return
        if cnt[i] > cnt[i - 1]:
            print('NO')
            return
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

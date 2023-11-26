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
    n, x = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    sa = sorted((ai, i) for i, ai in enumerate(a))
    sb = sorted((bi, i) for i, bi in enumerate(b))
    ans = [0 for i in range(n)]
    for k in range(x):
        bi, i = sb[k]
        ai, j = sa[n - x + k]
        ans[j] = bi
    for k in range(n - x):
        bi, i = sb[x + k]
        ai, j = sa[k]
        ans[j] = bi
    cnt = 0
    for ai, ansi in zip(a, ans):
        if ai > ansi:
            cnt += 1
    if cnt != x:
        print('NO')
    else:
        print('YES')
        print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

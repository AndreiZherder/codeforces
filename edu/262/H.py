from collections import Counter
from os import path
from sys import stdin, stdout


if path.exists("../../templates/input.txt"):
    stdin = open("../../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    INF = 10 ** 20
    s = input()
    nb, ns, nc = [int(num) for num in input().split()]
    pb, ps, pc = [int(num) for num in input().split()]
    r = int(input())
    cnt = Counter(s)
    cb = cnt['B']
    cs = cnt['S']
    cc = cnt['C']
    ans = 0
    ans += min(nb // cb if cb != 0 else INF, ns // cs if cs != 0 else INF, nc // cc if cc != 0 else INF)
    nb -= ans * cb
    ns -= ans * cs
    nc -= ans * cc
    """
    TTTTFFFF
        |
    """
    def check(mid: int) -> bool:
        need_b = mid * cb - min(mid * cb, nb)
        need_s = mid * cs - min(mid * cs, ns)
        need_c = mid * cc - min(mid * cc, nc)
        return need_b * pb + need_s * ps + need_c * pc <= r

    left = 0
    right = 10 ** 13
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    if left - 1 == -1:
        x = 0
    else:
        x = left - 1
    print(ans + x)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

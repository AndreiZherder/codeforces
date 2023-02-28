import sys
import time

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def get_k(x: int, r: int) -> int:
    k = 0
    while x <= r:
        k += 1
        x *= 2
    return k


def check3(x: int, k: int, r: int) -> bool:
    x *= 3
    if k > 2:
        x *= 1 << (k - 2)
    return x <= r


def solution():
    mod = 998244353
    l, r = (int(num) for num in input().split())

    mx = get_k(l, r)

    nums = [l]

    x = r
    for i in range(mx - 1):
        x //= 2

    x = max(x, l)

    ans = 0
    for num in range(l, x + 1):
        if check3(num, mx, r):
            ans = (ans + 1 + mx - 1) % mod
        else:
            ans = (ans + 1) % mod

    print(mx, ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

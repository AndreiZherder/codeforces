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


def sn(a1: int, an: int, n: int) -> int:
    return (a1 + an) * n // 2


def solution():
    mod = 998244353
    n, k = [int(num) for num in input().split()]
    perm = [int(num) for num in input().split()]
    if k == 1:
        print(n)
        print(1)
        return
    i = 0
    while perm[i] <= n - k:
        i += 1
    j = n - 1
    while perm[i] <= n - k:
        j -= 1
    cur = 1
    ans = 1
    while i <= j:
        if perm[i] <= n - k:
            cur += 1
        else:
            ans = ans * cur % mod
            cur = 1
        i += 1
    print(sn(n, n - k + 1, k), ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

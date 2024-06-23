from functools import lru_cache
from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    @lru_cache(None)
    def dp(i: int, double: int) -> int:
        if i == n - 1:
            if double == 0:
                return 10 ** 20
            else:
                return int(s[i])
        ans = 10 ** 20
        ans = min(ans, int(s[i]) + dp(i + 1, double))
        ans = min(ans, int(s[i]) * dp(i + 1, double))
        if not double:
            if i == n - 2:
                return int(s[i:])
            ans = min(ans, int(s[i:i + 2]) + dp(i + 2, 1))
            ans = min(ans, int(s[i:i + 2]) * dp(i + 2, 1))
        return ans

    n = int(input())
    s = input()
    print(dp(0, 0))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

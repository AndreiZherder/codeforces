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
    def dp(i: int, prev_v: int) -> int:
        if (i, prev_v) in cache:
            ans = cache[(i, prev_v)]
        elif i == t - 1:
            if abs(v2 - prev_v) > d:
                ans = -10 ** 20
            else:
                ans = v2
        else:
            ans = -10 ** 20
            for v in range(max(0, prev_v - d), prev_v + d + 1):
                ans = max(ans, v + dp(i + 1, v))
        cache[(i, prev_v)] = ans
        return ans

    v1, v2 = [int(num) for num in input().split()]
    t, d = [int(num) for num in input().split()]
    cache = dict()
    print(v1 + dp(1, v1))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

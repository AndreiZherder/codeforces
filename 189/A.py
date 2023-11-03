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
    n, a, b, c = [int(num) for num in input().split()]
    INF = 10 ** 20
    dp = [-INF for i in range(4001)]
    dp[a] = 1
    dp[b] = 1
    dp[c] = 1
    for i in range(n + 1):
        if dp[i] != -INF:
            for x in (a, b, c):
                if i + x <= n:
                    dp[i + x] = max(dp[i + x], dp[i] + 1)
    print(dp[n])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

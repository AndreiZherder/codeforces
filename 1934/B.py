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
    n = int(input())
    ans = 0
    if n > 100:
        x = n - 100
        ans += x // 15
        x %= 15
        n = 100 + x
    dp = [10 ** 20 for i in range(n + 1)]
    for coin in [1, 3, 6, 10, 15]:
        if coin <= n:
            dp[coin] = 1
    for i in range(1, n + 1):
        for coin in [1, 3, 6, 10, 15]:
            if i - coin > 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    print(ans + dp[n])


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

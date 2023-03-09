import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, k = (int(num) for num in input().split())
    a = [int(num) for num in input().split()] + [0]
    a = [[a[j] >> div for j in range(n + 1)] for div in range(32)]
    dp = [[0 for j in range(n + 1)] for div in range(32)]
    for j in range(n - 1, -1, -1):
        for div in range(30, -1, -1):
            dp[div][j] = max(a[div][j] - k + dp[div][j + 1],
                             a[div + 1][j] + dp[div + 1][j + 1])
    print(dp[0][0])


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

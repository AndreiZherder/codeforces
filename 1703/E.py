import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(num) for num in input()])
    ans = 0
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            x = a[i][j] + a[j][n - i - 1] + a[n - i - 1][n - j - 1] + a[n - j - 1][i]
            ans += 2 if x == 2 else x % 2
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

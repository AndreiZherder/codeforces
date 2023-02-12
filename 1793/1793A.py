import sys

input = sys.stdin.readline


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    a, b = (int(num) for num in input().split())
    n, m = (int(num) for num in input().split())
    if a <= b:
        x = n // (m + 1)
        ans = a * x * m
        n -= x * (m + 1)
        ans += a * n
        print(ans)
    elif a * m <= b * (m + 1):
        x = n // (m + 1)
        ans = a * x * m
        n -= x * (m + 1)
        ans += b * n
        print(ans)
    else:
        print(n * b)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

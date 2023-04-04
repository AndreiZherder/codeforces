import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, x1, y1, x2, y2 = (int(num) for num in input().split())
    print(abs(min(x1 - 1, n - x1, y1 - 1, n - y1) - min(x2 - 1, n - x2, y2 - 1, n - y2)))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

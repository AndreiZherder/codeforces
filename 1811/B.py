import sys
from random import randrange

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def main():
    def solution():
        n, x1, y1, x2, y2 = (int(num) for num in input().split())

        half = n // 2

        dx = min(abs(half - x1 + 1), abs(half - x1))
        dy = min(abs(half - y1 + 1), abs(half - y1))
        circle1 = max(dx, dy)

        dx = min(abs(half - x2 + 1), abs(half - x2))
        dy = min(abs(half - y2 + 1), abs(half - y2))
        circle2 = max(dx, dy)
        ans.append(abs(circle1 - circle2))

    t = int(input())
    ans = []
    while t:
        solution()
        t -= 1
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()

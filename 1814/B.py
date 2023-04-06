import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    a, b = (int(num) for num in input().split())
    best = a + b
    for i in range(1, 100000):
        best = min(best, i - 1 + (a + i - 1) // i + (b + i - 1) // i)
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

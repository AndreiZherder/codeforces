import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    b = [int(num) for num in input().split()]
    a = [10 ** 20 for i in range(n)]
    h = [(num, i) for i, num in enumerate(b)]
    h.sort()
    for num, i in h:
        a[i] = min(a[i], num)
        a[i + 1] = min(a[i + 1], num)
    print(*a)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

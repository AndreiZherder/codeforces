import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]

    mx = -10 ** 20
    for i in range(1, n - 1):
        if a[i] < a[i - 1]:
            delta = a[i - 1] - a[i]
            a[i] += delta
            a[i + 1] += delta
        mx = max(mx, a[i])
    mx = max(mx, a[0], a[n - 1])

    if a[n - 1] >= a[n - 2]:
        print('YES')
        return

    for i in range(n - 1, 0, -1):
        delta = mx - a[i]
        a[i] += delta
        a[i - 1] += delta
    if a[0] <= a[1]:
        print('YES')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

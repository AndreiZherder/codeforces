import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input()) + 2
    a = [0] + [int(num) for num in input().split()] + [1440]
    cnt = 0
    for i in range(1, n):
        cnt += (a[i] - a[i - 1]) // 120
    if cnt >= 2:
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

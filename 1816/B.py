import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [[0 for j in range(n)] for i in range(2)]
    i = 1
    for k in range(n):
        a[i][k] = k + 1
        i ^= 1
    a[0][0] = 2 * n
    i = 1
    x = 2 * n - 1
    for k in range(n - 1, 0, -1):
        a[i][k] = x
        i ^= 1
        x -= 1
    print(*a[0])
    print(*a[1])


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

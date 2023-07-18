from math import ceil, sqrt
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def main():
    a = []
    n = ceil((-1 + sqrt(1 + 8 * 1000000)) / 2)
    a = [[0 for j in range(n + 1)] for i in range(n + 1)]
    pref = [[0 for j in range(n + 1)] for i in range(n + 1)]
    prefd = [[0 for j in range(n + 1)] for i in range(n + 1)]
    cur = 1
    i = 0
    size = 1
    while cur <= 1000000:
        j = 0
        while cur <= 1000000 and j < size:
            a[i][j] = cur
            if i == 0:
                prefd[i][j] = cur ** 2
                pref[i][j] = cur ** 2
            elif j == 0:
                prefd[i][j] = cur ** 2
                pref[i][j] = pref[i - 1][j] + cur ** 2
            else:
                prefd[i][j] = prefd[i - 1][j - 1] + cur ** 2
                pref[i][j] = prefd[i - 1][j - 1] + pref[i - 1][j] + cur ** 2
            cur += 1
            j += 1
        i += 1
        size += 1
    t = int(input())
    while t:
        n = int(input())
        i = ceil((-1 + sqrt(1 + 8 * n)) / 2) - 1
        j = n - a[i][0]
        print(pref[i][j])
        t -= 1


if __name__ == '__main__':
    main()

from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append([int(num) for num in input().split()])
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            f = []
            f.append(j - 1 >= 0 and a[i][j - 1] != 0 and a[i][j] != 0 and a[i][j - 1] >= a[i][j])
            f.append(i - 1 >= 0 and a[i - 1][j] != 0 and a[i][j] != 0 and a[i - 1][j] >= a[i][j])
            if any(f):
                print(-1)
                return

    for i in range(n - 2, 0, -1):
        for j in range(m - 2, 0, -1):
            if a[i][j] == 0:
                x = min(a[i][j + 1] - 1, a[i + 1][j] - 1)
                if x <= a[i - 1][j] or x <= a[i][j - 1]:
                    print(-1)
                    return
                a[i][j] = x
    print(sum(sum(a[i]) for i in range(n)))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

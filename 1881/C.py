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
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    ans = 0
    for i in range(n // 2):
        for j in range(n // 2):
            x1 = a[i][j]
            x2 = a[j][n - 1 - i]
            x3 = a[n - 1 - i][n - 1 - j]
            x4 = a[n - 1 - j][i]
            best = ord(max(x1, x2, x3, x4))
            ans += sum(best - ord(x) for x in (x1, x2, x3, x4))
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

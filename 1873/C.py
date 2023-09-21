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
    a = []
    for i in range(10):
        a.append(input())
    ans = 0
    for i in range(10):
        for j in range(10):
            if a[i][j] == 'X':
                ans += (min(i + 1, 10 - i, j + 1, 10 - j))
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

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
    s = input()
    x = 0
    y = 0
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            x += 1
        else:
            y += 1
    ans = [0 for i in range(n + 1)]
    for i in range(x, x + 2 * y + 1, 2):
        ans[i] = 1
        if n % 2 == 1:
            ans[i + 1] = 1
    print(''.join(map(str, ans)))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

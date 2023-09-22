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
    s = input()
    n = len(s)
    x = int(input())
    ans = ['1' for i in range(n)]
    for i, c in enumerate(s):
        if c == '0':
            if i - x >= 0:
                ans[i - x] = '0'
            if i + x < n:
                ans[i + x] = '0'
    for i, c in enumerate(s):
        if c == '1':
            if (i - x < 0 or ans[i - x] == '0') and (i + x >= n or ans[i + x] == '0'):
                print(-1)
                return
    print(''.join(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

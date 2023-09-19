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
    n, k = [int(num) for num in input().split()]
    s = input()
    if k % 2 == 0:
        print(''.join(sorted(s)))
    else:
        ans = ['' for i in range(n)]
        ans[::2] = sorted(s[::2])
        ans[1::2] = sorted(s[1::2])
        print(''.join(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

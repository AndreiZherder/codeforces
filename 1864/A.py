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
    x, y, n = [int(num) for num in input().split()]
    ans = [0 for i in range(n)]
    ans[0] = x
    ans[-1] = y
    cur = y
    for i in range(n - 2):
        cur -= (i + 1)
        ans[n - 2 - i] = cur
    if ans[1] - ans[0] <= ans[2] - ans[1]:
        print(-1)
    else:
        print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

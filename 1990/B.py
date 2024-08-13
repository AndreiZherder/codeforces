from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, x, y = [int(num) for num in input().split()]
    ans = [1 for i in range(n)]
    cur = -1
    for i in range(x, n):
        ans[i] = cur
        cur *= -1
    cur = -1
    for i in range(y - 2, -1, -1):
        ans[i] = cur
        cur *= -1
    print(*ans)





def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

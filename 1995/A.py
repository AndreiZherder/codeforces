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
    n, k = [int(num) for num in input().split()]
    if k == 0:
        print(0)
        return
    if k <= n:
        print(1)
        return
    ans = 1
    k -= n
    m = n
    while k > 0:
        m -= 1
        if k <= m:
            print(ans + 1)
            return
        elif k <= 2 * m:
            print(ans + 2)
            return
        k -= 2 * m
        ans += 2


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

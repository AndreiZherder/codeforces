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


def sn(a1: int, an: int, n: int) -> int:
    return (a1 + an) * n // 2


def solution():
    n, k, x = [int(num) for num in input().split()]
    ans = True
    if k > n:
        ans = False
    if sn(n, n - k + 1, k) < x:
        ans = False
    if sn(1, k, k) > x:
        ans = False
    print('YES' if ans else 'NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

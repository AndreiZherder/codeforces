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
    n, x = [int(num) for num in input().split()]
    ans = 0
    for a in range(1, n + 1):
        b = 1
        while a * b <= n and a + b <= x:
            ans += min(x - (a + b), (n - a * b) // (a + b))
            b += 1
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

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
    x, y = [int(num) for num in input().split()]
    n = int(input())
    mod = 10 ** 9 + 7
    d = {
        0: lambda x, y: x % mod,
        1: lambda x, y: y % mod,
        2: lambda x, y: (y - x) % mod,
        3: lambda x, y: -x % mod,
        4: lambda x, y: -y % mod,
        5: lambda x, y: (-y + x) % mod,
    }
    print(d[(n - 1) % 6](x, y))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

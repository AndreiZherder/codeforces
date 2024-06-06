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


def dec_to_bin(x: int, n: int) -> str:
    return bin(x)[2:].zfill(n)


def solution():
    x, y = [int(num) for num in input().split()]
    x = bin(x)[2:]
    y = bin(y)[2:]
    m = max(len(x), len(y))
    x = x.zfill(m)
    y = y.zfill(m)
    cur = 0
    for a, b in zip(reversed(x), reversed(y)):
        if a == b:
            cur += 1
        else:
            break
    print(2 ** cur)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

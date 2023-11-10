import string
from itertools import chain
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


def dec_to_bin(x: int, n: int) -> str:
    return bin(x)[2:].zfill(n)


def solution():
    mod = 10 ** 9 + 7
    s = input()
    d = {c: i for i, c in enumerate((chain.from_iterable(('0123456789', string.ascii_uppercase, string.ascii_lowercase, '-_'))))}
    ans = 1
    for c in s:
        for bit in dec_to_bin(d[c], 6):
            if bit == '0':
                ans = (ans * 3) % mod
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

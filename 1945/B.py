from math import gcd
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


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    a, b, m = [int(num) for num in input().split()]
    print(ceil(m + 1, a) + ceil(m + 1, b))



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

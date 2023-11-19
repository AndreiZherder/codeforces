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
    x = s.count('B')
    if k == x:
        print(0)
    elif k > x:
        a = [i for i, c in enumerate(s) if c == 'A']
        print(1)
        print(a[k - x - 1] + 1, 'B')
    else:
        a = [i for i, c in enumerate(s) if c == 'B']
        print(1)
        print(a[x - k - 1] + 1, 'A')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

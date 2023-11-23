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
    n = int(input())
    if n <= 5:
        print(-1)
    else:
        print(1, 2)
        print(2, 3)
        print(2, 4)
        for i in range(5, n + 1):
            print(1, i)
    for i in range(1, n):
        print(i, i + 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

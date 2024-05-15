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
    r = int(input())
    x = r
    y = 0
    ans = 0
    while x > 0:
        while x ** 2 + y ** 2 < (r + 1) ** 2:
            if x ** 2 + y ** 2 >= r ** 2:
                ans += 1
            y += 1
        x -= 1
        y -= 1
    print(ans * 4)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

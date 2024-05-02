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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    n = int(input())
    x = [int(num) for num in input().split()]
    a = [x[0] + 1]
    for i in range(n - 1):
        if i == n - 2:
            y = a[-1] + x[i]
        else:
            y = ceil(x[i + 1], a[-1]) * a[-1] + x[i]
        a.append(y)
    print(*a)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

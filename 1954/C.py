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
    x = list(input())
    y = list(input())
    n = len(x)
    i = 0
    while i < n and x[i] == y[i]:
        i += 1
    start = i
    i += 1
    while i < n:
        if x[start] >= y[start]:
            x[i], y[i] = min(x[i], y[i]), max(x[i], y[i])
        else:
            x[i], y[i] = max(x[i], y[i]), min(x[i], y[i])
        i += 1
    print(''.join(x))
    print(''.join(y))




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

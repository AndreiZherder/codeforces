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
    h, m = [int(num) for num in input().split(':')]
    if h < 12:
        if h == 0:
            h = 12
        h = str(h)
        m = str(m)
        if len(h) == 1:
            h = '0' + h
        if len(m) == 1:
            m = '0' + m
        print(f'{h}:{m} AM')
    else:
        h -= 12
        if h == 0:
            h = 12
        h = str(h)
        m = str(m)
        if len(h) == 1:
            h = '0' + h
        if len(m) == 1:
            m = '0' + m
        print(f'{h}:{m} PM')



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

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
    if n < 28:
        print(''.join(['aa', chr(n - 2 + ord('a') - 1)]))
    elif n < 53:
        print(''.join(['a', chr(n - 27 + ord('a') - 1), 'z']))
    else:
        print(''.join([chr(n - 52 + ord('a') - 1), 'zz']))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

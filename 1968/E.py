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
    n = int(input())
    if n == 2:
        print(1, 1)
        print(2, 2)
    elif n == 3:
        print(1, 1)
        print(3, 3)
        print(1, 2)
    else:
        print(1, 1)
        print(n, n)
        print(1, 2)
        print(n, 2)
        j = 1
        for k in range(n - 4):
            j += 1
            print(n, j + 1)
    print()

def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

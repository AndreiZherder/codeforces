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
    if n == 1:
        print('YES')
        return
    while n != 1:
        for i in range(31, 1, -1):
            d = int(bin(i)[2:])
            if n % d == 0:
                n //= d
                break
        else:
            print('NO')
            return
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

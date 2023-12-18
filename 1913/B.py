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
    s = input()
    n = len(s)
    zeroes = s.count('0')
    ones = n - zeroes
    for i in range(n):
        if s[i] == '0':
            if not ones:
                print(n - i)
                return
            else:
                ones -= 1
        else:
            if not zeroes:
                print(n - i)
                return
            else:
                zeroes -= 1
    print(0)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

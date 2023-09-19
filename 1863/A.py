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
    n, a, q = [int(num) for num in input().split()]
    s = input()
    c1 = a
    c2 = a
    if c1 >= n:
        print('YES')
        return
    for x in s:
        if x == '+':
            c1 += 1
            c2 += 1
        else:
            c1 -= 1
        if c1 >= n:
            print('YES')
            return
    if c2 >= n:
        print('MAYBE')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

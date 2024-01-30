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
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    order = sorted(range(n), key=lambda i: a[i])
    print(*[a[i] for i in order])
    print(*[b[i] for i in order])


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

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
    a = []
    for i in range(n):
        a.append([int(num) for num in input().split()])
    a.sort()
    last = 0
    ans = 0
    for ai, bi in a:
        if bi < last:
            last = ai
            ans = ai
        else:
            last = bi
            ans = bi
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

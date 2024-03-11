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
    n, m, x = [int(num) for num in input().split()]
    x -= 1
    xs, xs1 = {x}, set()
    for i in range(m):
        r, c = input().split()
        r = int(r)
        if c == '0':
            for x in xs:
                xs1.add((x + r) % n)
        elif c == '1':
            for x in xs:
                xs1.add((x - r) % n)
        else:
            for x in xs:
                xs1.add((x + r) % n)
            for x in xs:
                xs1.add((x - r) % n)
        xs, xs1 = xs1, set()
    print(len(xs))
    print(*(x + 1 for x in sorted(xs)))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

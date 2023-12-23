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
    xs = []
    ys = []
    for i in range(n):
        x, y = [int(num) for num in input().split()]
        xs.append(x)
        ys.append(y)
    if all(x <= 0 for x in xs) or all(x >= 0 for x in xs) or all(y <= 0 for y in ys) or all(y >= 0 for y in ys):
        print('YES')
    else:
        print('NO')



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

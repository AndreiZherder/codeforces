from os import path
from sys import stdin, stdout


filename = '../../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, s = [int(num) for num in input().split()]
    w = [int(num) for num in input().split()]
    c = [int(num) for num in input().split()]
    totalw = 0
    totalc = 0
    best = 0
    j = 0
    for i in range(n):
        totalw += w[i]
        totalc += c[i]
        while totalw > s:
            totalw -= w[j]
            totalc -= c[j]
            j += 1
        best = max(best, totalc)
    print(best)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

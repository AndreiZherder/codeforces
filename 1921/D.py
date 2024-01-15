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
    n, m = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    a.sort()
    b.sort(reverse=True)
    c = [0 for i in range(n)]
    i1 = 0
    j1 = n - 1
    i2 = 0
    j2 = m - 1
    i3 = 0
    j3 = n - 1
    for k in range(n):
        if b[i2] - a[i1] >= a[j1] - b[j2]:
            c[i2] = b[i2]
            i1 += 1
            i2 += 1
            i3 += 1
        else:
            c[j3] = b[j2]
            j1 -= 1
            j2 -= 1
            j3 -= 1
    print(sum(abs(ai - ci) for ai, ci in zip(a, c)))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

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
    n, m, s, A, B = [int(num) for num in input().split()]
    a = sorted([int(num) for num in input().split()], reverse=True)
    b = sorted([int(num) for num in input().split()], reverse=True)
    i = -1
    j = m - 1
    wb = B * m
    costb = sum(b)
    wa = 0
    costa = 0
    best = 0
    while i < n and wa <= s:
        while j >= 0 and wb > s - wa:
            wb -= B
            costb -= b[j]
            j -= 1
        best = max(best, costa + costb)
        i += 1
        wa += A
        if i < n:
            costa += a[i]
    print(best)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

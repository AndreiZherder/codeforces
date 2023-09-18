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
    n, k, a, b = [int(num) for num in input().split()]
    a -= 1
    b -= 1
    xs = []
    ys = []
    for i in range(n):
        x, y = [int(num) for num in input().split()]
        xs.append(x)
        ys.append(y)
    best = abs(xs[b] - xs[a]) + abs(ys[b] - ys[a])
    best1 = best
    best2 = best
    for i in range(k):
        best1 = min(best1, abs(xs[a] - xs[i]) + abs(ys[a] - ys[i]))
        best2 = min(best2, abs(xs[b] - xs[i]) + abs(ys[b] - ys[i]))
    print(min(best, best1 + best2))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

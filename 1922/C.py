from itertools import accumulate
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
    xs = [int(num) for num in input().split()]
    forward = [0 for i in range(n)]
    forward[1] = 1
    backward = [0 for i in range(n)]
    backward[1] = 1

    for i in range(2, n):
        if xs[i] - xs[i - 1] < xs[i - 1] - xs[i - 2]:
            forward[i] = 1
        else:
            forward[i] = xs[i] - xs[i - 1]
    forward_pref = list(accumulate(forward))

    xs.reverse()
    for i in range(2, n):
        if xs[i] - xs[i - 1] > xs[i - 1] - xs[i - 2]:
            backward[i] = 1
        else:
            backward[i] = -(xs[i] - xs[i - 1])
    backward_pref = list(accumulate(backward))

    m = int(input())
    for i in range(m):
        x1, x2 = [int(num) - 1 for num in input().split()]
        if x1 < x2:
            print(forward_pref[x2] - forward_pref[x1])
        else:
            x1, x2 = n - x1 - 1, n - x2 - 1
            print(backward_pref[x2] - backward_pref[x1])


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

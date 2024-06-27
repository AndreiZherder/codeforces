from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
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
    score1 = 0
    score2 = 0
    for x, y in zip(a, b):
        if x == 1 and (y == 0 or y == -1):
            score1 += 1
        if (x == 0 or x == -1) and y == 1:
            score2 += 1
    for x, y in zip(a, b):
        if x == 1 and y == 1:
            if score1 <= score2:
                score1 += 1
            else:
                score2 += 1
        if x == -1 and y == -1:
            if score1 <= score2:
                score2 -= 1
            else:
                score1 -= 1
    print(min(score1, score2))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

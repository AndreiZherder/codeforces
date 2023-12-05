from collections import Counter
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
    counter = Counter(input())
    mx = max(counter.values())
    sum_of_others = sum(counter.values()) - mx
    if mx - sum_of_others >= 0:
        print(mx - sum_of_others)
    else:
        print(n % 2)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

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
    a1, a2, b1, b2 = [int(num) for num in input().split()]
    ans = 0
    if (a1 >= b1 and a2 > b2) or (a1 > b1 and a2 >= b2):
        ans += 2
    if (a1 >= b2 and a2 > b1) or (a1 > b2 and a2 >= b1):
        ans += 2
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

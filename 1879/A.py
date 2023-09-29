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
    s = []
    e = []
    for i in range(n):
        si, ei = [int(num) for num in input().split()]
        s.append(si)
        e.append(ei)
    if any(s[i] >= s[0] and e[i] >= e[0] for i in range(1, n)):
        print(-1)
    else:
        print(s[0])


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

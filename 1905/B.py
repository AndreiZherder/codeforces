from collections import defaultdict
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
    g = defaultdict(list)
    for i in range(n - 1):
        u, v = [int(num) - 1 for num in input().split()]
        g[u].append(v)
        g[v].append(u)
    print((sum(len(g[v]) == 1 for v in g) + 1) // 2)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

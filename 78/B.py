from collections import deque
from itertools import cycle
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
    last3 = deque(maxlen=3)
    c = cycle('ROYGBIV')
    ans = []
    for i in range(n):
        x = next(c)
        while x in last3 or x in ans[:3]:
            x = next(c)
        last3.append(x)
        ans.append(x)
    print(''.join(ans))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

from collections import Counter
from os import path
from random import getrandbits
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


RANDOM = getrandbits(32)


class Int(int):
    def __hash__(self):
        return super().__hash__() ^ RANDOM


def solution():
    n = int(input())
    c = Counter((Int(num) for num in input().split()))
    if any(v > 2 for v in c.values()):
        print('NO')
    else:
        print('YES')
        ans1 = []
        ans2 = []
        for num, v in sorted(c.items()):
            ans1.append(num)
            if v == 2:
                ans2.append(num)
        print(len(ans1))
        print(*ans1)
        print(len(ans2))
        print(*reversed(ans2))



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

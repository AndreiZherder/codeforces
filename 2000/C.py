from os import path
from random import getrandbits
from sys import stdin, stdout


filename = '../templates/input.txt'
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
    nums = [Int(num) for num in input().split()]
    m = int(input())
    words = []
    for i in range(m):
        words.append(input())
    for word in words:
        d1 = dict()
        d2 = dict()
        if len(word) != n:
            print('NO')
            continue
        for num, c in zip(nums, word):
            if num in d1:
                if d1[num] != c or c not in d2 or d2[c] != num:
                    print('NO')
                    break
            if c in d2:
                if d2[c] != num or num not in d1 or d1[num] != c:
                    print('NO')
                    break
            d1[num] = c
            d2[c] = num
        else:
            print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

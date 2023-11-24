from bisect import bisect_right, bisect_left
from itertools import combinations, permutations, product
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
    a = [10 ** 18]
    for i in range(1, 4):
        for comb in combinations(range(18), i):
            for prod in product(range(1, 10), repeat=i):
                cur = 0
                for j, digit in zip(comb, prod):
                    cur += digit * 10 ** j
                a.append(cur)


    a.sort()
    while n:
        l, r = [int(num) for num in input().split()]
        print(bisect_right(a, r) - bisect_left(a, l))
        n -= 1



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

from heapq import heappush, heappop
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
    h, n = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    c = [int(num) for num in input().split()]
    heap = []
    for ai, ci in zip(a, c):
        heappush(heap, (1, ai, ci))
    while h > 0:
        step, ai, ci = heappop(heap)
        h -= ai
        heappush(heap, (step + ci, ai, ci))
    print(step)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

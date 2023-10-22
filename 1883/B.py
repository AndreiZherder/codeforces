from collections import Counter, deque
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
    n, k = [int(num) for num in input().split()]
    cnt = Counter(input())
    evens = []
    odds = []
    total_evens = 0
    total_odds = 0
    for v in cnt.values():
        if v % 2 == 0:
            evens.append(v)
            total_evens += v
        else:
            odds.append(v)
            total_odds += v
    k = n - k
    if total_evens >= k:
        print('YES')
        return
    k -= total_evens
    if total_odds - len(odds) + 1 >= k:
        print('YES')
        return
    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

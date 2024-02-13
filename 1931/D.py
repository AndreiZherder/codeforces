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
    n, x, y = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    c = Counter()
    ans = 0
    for num in nums:
        ans += c[((x - num % x) % x, num % y)]
        c[(num % x, num % y)] += 1
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

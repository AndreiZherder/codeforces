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
    n = int(input())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    ans = 0
    mn = 10 ** 20
    for ai, bi in zip(a, b):
        ans += abs(ai - bi)
        if min(ai, bi) <= b[-1] <= max(ai, bi):
            mn = 0
        mn = min(mn, abs(ai - b[-1]), abs(bi - b[-1]))
    ans += mn + 1
    print(ans)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

from collections import defaultdict
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
    n, m = [int(num) for num in input().split()]
    s = input()
    indexes = [int(num) for num in input().split()]
    s1 = input()
    ans = [chr(ord('z') + 1) for i in range(n)]
    for i, c in zip(sorted(set(indexes)), sorted(s1)):
        ans[i - 1] = min(ans[i - 1], c)
    print(''.join(ans[i] if ans[i] != chr(ord('z') + 1) else s[i] for i in range(n)))



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()

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
    m = int(input())
    x = min(int(num) for num in input().split())
    n = int(input())
    a = sorted((int(num) for num in input().split()))
    ans = 0
    while a:
        for i in range(x):
            if a:
                ans += a.pop()
        for i in range(2):
            if a:
                a.pop()
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
